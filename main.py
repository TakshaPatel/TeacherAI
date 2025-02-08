import streamlit as st
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

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

st.title("Your :green[Friendly] Better :blue[AI] Teacher:")
st.text("By Taksha           (Please know I do not control the ads shown)")

user_prompt = st.text_input("Write your prompt:")
response_text = ""

if st.button("🎙 Speak to it (might not work, idk)"):
    user_prompt = speech_to_text()

# Generate Response
if user_prompt:
    response = model.generate_content(
        f"You have to be good at teaching, do not use big vocab words. Do not be mean to me. You have to be extremely helpful: {user_prompt}",
        stream=True
    )
    response_text = ""
    for chunk in response:
        if hasattr(chunk, "text") and chunk.text:
            response_text += chunk.text

st.text_area("Teacher says:", response_text, height=375)
st.text("Learn what you need in minutes: It is very friendly, 👍👍👍")

ad_code = """
<iframe src="//www.highperformanceformat.com/636d00d3d45691d4d185b42d691c47f3/invoke.js"
        width="728" height="90" style="border:none;overflow:hidden" scrolling="no">
</iframe>
"""
st.components.v1.html(ad_code, height=90)
