import streamlit as st
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# Configure Gemini API
genai.configure(api_key="AIzaSyA4EXQew6Oz1ON-O05DGXRtLJIIt-dFR9Y")
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

#UI
st.title("Your :green[Friendly] Better :blue[AI] Teacher:")
st.text("By Taksha...")
user_prompt = st.text_input("Write your prompt:")
response_text = ""

if st.button("🎙 Speak to it (might not work, idk)"):
    user_prompt = speech_to_text()
if user_prompt:
    response = model.generate_content(
        "You have to be good at teaching, do not use big vocab words. Do not be mean to me You have to be Extreamly helpful, try to also add jokes at the end of your paragraphs that relate with the topic That I say: " + user_prompt
    )
    response_text = response.text


st.text_area("Teacher says:", response_text, height=200)

st.text("Learn what you need in minutes: It is very friendly, 👍👍👍")