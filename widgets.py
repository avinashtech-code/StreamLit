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




from datetime import date, time

st.title("Date, Time & Color Picker Demo")

# ===================================================
# st.date_input()
# ===================================================

st.header("st.date_input()")

# 1. Simple Date Input
selected_date = st.date_input("Select Date")
st.write("Selected Date:", selected_date)

# ===================================================
# st.time_input()
# ===================================================

st.header("st.time_input()")

# 1. Simple Time Input
selected_time = st.time_input("Select Time")
st.write("Selected Time:", selected_time)


# -----------------------------
# 3. Color Picker
# -----------------------------
selected_color = st.color_picker(
    "Choose Your Favorite Color",
    value="#00FF00"
)

st.write("Selected Color:", selected_color)

# Change text color using the selected color
st.markdown(
    f"<h2 style='color:{selected_color};'>Hello Avinash </h2>",
    unsafe_allow_html=True
)
