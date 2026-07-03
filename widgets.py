import streamlit as st

st.title("Input Widgets Demo")

# Checkbox
agree = st.checkbox("I Agree to the Terms")
st.write("Checkbox:", agree)

st.divider()

# Radio
gender = st.radio(
    "Select Gender",
    ["Male", "Female", "Other"]
)
st.write("Selected Gender:", gender)

st.divider()

# Selectbox
course = st.selectbox(
    "Select Course",
    ["Python", "Java", "C++", "Machine Learning"]
)
st.write("Selected Course:", course)

st.divider()

# Multiselect
skills = st.multiselect(
    "Select Your Skills",
    ["Python", "Java", "SQL", "Pandas", "NumPy", "Streamlit"]
)


st.divider()

# Slider
age = st.slider(
    "Select Your Age",
    min_value=18,
    max_value=60,
    value=21
)
st.write("Age:", age)
