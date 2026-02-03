import streamlit as st
from PIL import Image
from image_caption import generate_caption
from story_generator import generate_story, elevate_caption
from tts import text_to_speech
import atexit
import glob
import os

if "caption" not in st.session_state:
    st.session_state.caption = None

if "story" not in st.session_state:
    st.session_state.story = None

if "audio_file" not in st.session_state:
    st.session_state.audio_file = None

if "last_image" not in st.session_state:
    st.session_state.last_image = None



def cleanup_audio():
    for f in glob.glob("audio_*.mp3"):
        os.remove(f)
    print("Cleaned up audio files")

atexit.register(cleanup_audio)

st.set_page_config(page_title="Image Generator")

st.title("Image Generator")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    uploaded_file.seek(0)
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    tone = st.selectbox("Select a tone", ["reflective", "elevation", "motivational","emotional", "hopeful"])

    if st.session_state.get("last_image") != uploaded_file.name:
       st.session_state.caption = None
       st.session_state.story = None
       st.session_state.audio_file = None
       st.session_state.last_image = uploaded_file.name


    if st.button("Generate Story"):
        with st.spinner("Generating Caption..."):
          raw_caption = generate_caption(image)
          st.session_state.caption=elevate_caption(raw_caption)

        with st.spinner("Generating story..."):
            st.session_state.story = generate_story(
                image_caption=st.session_state.caption,
                tone=tone,
            )

        with st.spinner("Generating audio..."):
            st.session_state.audio_file = text_to_speech(
                st.session_state.story
            )

if st.session_state.get("caption"):
    st.subheader("Generated Caption")
    st.write(st.session_state.caption)

if st.session_state.get("story"):
    st.subheader("Generated Story")
    st.write(st.session_state.story)

if st.session_state.get("audio_file"):
    st.subheader("Listen to the story")
    st.audio(st.session_state.audio_file)

    with open(st.session_state.audio_file, "rb") as f:
        st.download_button(
            label="Download Audio",
            data=f,
            file_name="image_story.mp3",
            mime="audio/mpeg"
        )
