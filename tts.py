from gtts import gTTS
import os
import uuid 

def text_to_speech(text: str) -> str:
    """
    converts text into speec and saves it as an mp3 file.
    Returns the file.
    """

    filename= f"audio_{uuid.uuid4()}.mp3"
    tts=gTTS(text=text, lang="en")
    tts.save(filename)
    return filename