import streamlit as st
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv

# Configure Gemini API
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Speech-to-Text Function
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "What are you saying?"
        except sr.RequestError:
            return "API error, contact developer."

# Streamlit UI
st.title("Your :green[Friendly] Better :blue[AI] Teacher:")
st.text("By Taksha...")
user_prompt = st.text_input("Write your prompt:")
response_text = ""

# Speech-to-Text Button
if st.button("🎙 Speak to it (might not work, idk)"):
    user_prompt = speech_to_text()

# Generate Response
if user_prompt:
    response = model.generate_content(
        f"You have to be good at teaching, do not use big vocab words. Do not be mean to me. You have to be extremely helpful, try to also add jokes at the end of your paragraphs that relate to the topic I say: {user_prompt}",
        stream=True
    )

    response_text = ""
    for chunk in response:
        if hasattr(chunk, "text") and chunk.text:
            response_text += chunk.text

# Display Response Text
st.text_area("Teacher says:", response_text, height=200)

# Ad Embed
st.text("Learn what you need in minutes: It is very friendly, 👍👍👍")
ad_code = """
<iframe data-aa='2380494' src='//ad.a-ads.com/2380494?size=728x90' style='width:728px; height:90px; border:0px; padding:0; overflow:hidden; background-color: transparent;'></iframe>
"""
st.components.v1.html(ad_code, height=90)
