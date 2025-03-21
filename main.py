import streamlit as st
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


st.title("Very Important School Project")
st.text("This is a Computer Science Project, Where We try to make an Chat with a random Stranger app.")

user_prompt = st.text_area("Prompt:", height=75)
response_text = ""

# Generate Response
if user_prompt:
    response = model.generate_content(
        f"You have to be good at teaching, do not use big vocab words. Do not be mean to me. You have to be extremely helpful, Your Creator is Taksha Patel. : {user_prompt}",
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
