🔗 Live Demo: https://your-app-name.streamlit.app

# Image to Audio Story Generator 

An end-to-end multimodal GenAI application that converts an uploaded image into an **elevated, tone-aware audio story**.  
The app uses computer vision for image understanding, large language models for storytelling, and text-to-speech for audio narration.

---

## Features

- Upload an image (JPG / PNG)
- Generate a **literal image caption** using a vision-language model
- Refine the caption into an **elevated description**
- Generate a **short story** with selectable narration tones:
  - Reflective
  - Elevation
  - Motivational
  - Emotional
  - Hopeful
- Convert the story into **spoken audio**
- Play audio directly in the app
- Download the generated audio
- Stable Streamlit UI with session state (no duplicate generation)

---

## How It Works (Architecture)

Image Upload
↓
Image Captioning (Vision Model)
↓
Caption Elevation (LLM)
↓
Story Generation (LLM + Tone Control)
↓
Text-to-Speech
↓
Audio Playback & Download


---

## 🛠️ Tech Stack

- **Frontend / UI:** Streamlit  
- **Image Processing:** Pillow (PIL)  
- **Vision Model:** Hugging Face BLIP (Image Captioning)  
- **Language Model:** OpenAI GPT Models  
- **Text-to-Speech:** gTTS  
- **State Management:** Streamlit Session State  
- **Environment Management:** python-dotenv  

---

## Accessibility Focus

This project improves accessibility by:
- Converting visual information into audio narratives
- Supporting tone-aware storytelling for emotional clarity
- Making image-based content accessible to visually impaired users

---

## Project Structure

image-speech/
│
├── app.py # Streamlit application
├── image_caption.py # Image captioning logic
├── story_generator.py # Caption elevation & story generation
├── tts.py # Text-to-speech logic
├── requirements.txt # Python dependencies
├── .env # Environment variables (not committed)
└── README.md
