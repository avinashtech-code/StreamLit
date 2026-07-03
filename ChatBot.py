import streamlit as st
import time

st.title("🤖 Chat Components Demo")

# User Input
prompt = st.chat_input("Ask me anything...")

if prompt:

    # User Message
    with st.chat_message("user"):
        st.write(prompt)

    # Assistant Message
    with st.chat_message("assistant"):

        placeholder = st.empty()

        response = "Hello! I am your AI Assistant."

        text = ""

        for char in response:

            text += char

            placeholder.markdown(text)

            time.sleep(0.05)
