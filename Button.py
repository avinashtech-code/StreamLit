import streamlit as st

if st.button("Current Time"):
    from datetime import datetime
    st.write(datetime.now())

if st.button("Random Number"):
    import random
    st.write(random.randint(1,100))

btn = st.button("Login")
st.write(btn)

if st.button("Click Me"):
    st.write("Hello World")

if st.button("Show Details"):
    st.write("Name : Avinash")
    st.write("Age : 20")

if st.button("Show Image"):
    st.image("cat.jpg")

if st.button("Generate Report"):
    create_pdf()

if st.button("Send Email"):
    send_mail()

if st.button("Submit"):
    st.success("Submitted Successfully")

if st.button("Celebrate"):
    st.balloons()

if st.button("Warning"):
    st.warning("Low Battery")


import webbrowser

if st.button("Google"):
    webbrowser.open("https://google.com")
