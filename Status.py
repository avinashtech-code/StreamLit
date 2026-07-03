import streamlit as st
import time

st.title("Status Elements Demo")

# ==========================
# Success
# ==========================
if st.button("Show Success"):
    st.success("Data saved successfully!")

st.divider()

# ==========================
# Error
# ==========================
if st.button("Show Error"):
    st.error("Something went wrong!")

st.divider()

# ==========================
# Info
# ==========================
if st.button("Show Info"):
    st.info("New update is available.")

st.divider()

# ==========================
# Spinner
# ==========================
if st.button("Load Data"):
    with st.spinner("Loading data..."):
        time.sleep(3)
    st.success("Data Loaded Successfully!")

st.divider()

# ==========================
# Progress Bar
# ==========================
if st.button("Start Progress"):
    progress = st.progress(0)

    for i in range(101):
        time.sleep(0.03)
        progress.progress(i)

    st.success("Completed!")

st.divider()


# ==========================
# Balloons
# ==========================
if st.button("Celebrate"):
    st.balloons()

st.divider()
