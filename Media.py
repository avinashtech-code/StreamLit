import streamlit as st


st.image(
    "E:\Downloads\WhatsApp Image 2026-06-07 at 6.18.17 PM.jpeg",
    caption= "cute ",
    width=None,
    use_container_width=True
)

st.image([
    "cat.jpg",
    "dog.jpg"
])

st.audio(
    data,
    format="audio/mp3",
    start_time=0
)

st.video(
    data,
    start_time=0
)
