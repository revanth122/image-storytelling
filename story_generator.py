import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def elevate_caption(caption: str) -> str:
    prompt = f"""
    You are an expert storyteller. You are given a caption and you need to elevate it.
    Caption: {caption}
    Elevate the caption to make it more engaging and interesting.
    Return the elevated caption.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are an expert storyteller."}, {"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()


def generate_story(
    image_caption: str,
    tone: str = "reflective",
    max_words: int = 120
) -> str:
    """
    Converts an image caption into a short story.
    """

    prompt = f"""
You are a storyteller creating an audio-friendly short story.

You Must follow these rules:
- Base the story on the image description.
- Do not invent specific identities or names.
- Keep the story concise and to the point.
- Avoid assumptions about emotions unless there are strongly implied.

Image description:
"{image_caption}"

Tone: {tone}
Tone guidance:
- elevation: calm, dignified, gently uplifting, reflective without exaggeration
- reflective: quiet and introspective
- motivational: encouraging and energizing
- calm: soothing and steady
- hopeful: optimistic and reassuring
- neutral descriptive: factual and observant

Write a short, vivid story (about {max_words} words).
Make it suitable for listening.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a thoughtful storyteller."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )

    return response.choices[0].message.content.strip()
