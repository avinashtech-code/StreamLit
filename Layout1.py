import streamlit as st

st.set_page_config(page_title="Layout Demo", layout="wide")

st.title("📐 Module 7 - Layout (Part 1)")

# ==========================================================
# SIDEBAR
# ==========================================================

st.header("1. st.sidebar()")

st.sidebar.title("🚀 Sidebar")

# Example 1 : Text Input
name = st.sidebar.text_input("Enter Name")

# Example 2 : Selectbox
course = st.sidebar.selectbox(
    "Course",
    ["Python", "Machine Learning", "GenAI"]
)

# Example 3 : Radio
gender = st.sidebar.radio(
    "Gender",
    ["Male", "Female"]
)

# Example 4 : Slider
age = st.sidebar.slider(
    "Age",
    18,
    60,
    20
)

# Example 5 : Button
if st.sidebar.button("Submit"):
    st.sidebar.success("Submitted Successfully!")

st.write("### Sidebar Output")
st.write("Name :", name)
st.write("Course :", course)
st.write("Gender :", gender)
st.write("Age :", age)

st.divider()

# ==========================================================
# COLUMNS
# ==========================================================

st.header("2. st.columns()")

# ----------------------------------------------------------
# Example 1 : Two Columns
# ----------------------------------------------------------

st.subheader("Example 1 : Two Columns")

col1, col2 = st.columns(2)

with col1:
    st.success("Column 1")

with col2:
    st.info("Column 2")

st.divider()

# ----------------------------------------------------------
# Example 2 : Three Columns
# ----------------------------------------------------------

st.subheader("Example 2 : Three Columns")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("😀")

with col2:
    st.write("🚀")

with col3:
    st.write("❤️")

st.divider()

# ----------------------------------------------------------
# Example 3 : Custom Width Columns
# ----------------------------------------------------------

st.subheader("Example 3 : Custom Ratio")

left, center, right = st.columns([1,2,1])

with left:
    st.success("1")

with center:
    st.warning("2")

with right:
    st.success("1")

st.divider()

# ----------------------------------------------------------
# Example 4 : Metrics Side by Side
# ----------------------------------------------------------

st.subheader("Example 4 : Dashboard Metrics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Users", "2500", "+200")

with c2:
    st.metric("Revenue", "₹50K", "+10%")

with c3:
    st.metric("Orders", "560", "-12")

st.divider()

# ----------------------------------------------------------
# Example 5 : Forms Side by Side
# ----------------------------------------------------------

st.subheader("Example 5 : Login Form")

left, right = st.columns(2)

with left:

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

with right:

    city = st.text_input("City")

    phone = st.text_input("Phone")

st.write("Username :", username)
st.write("City :", city)

st.divider()

# ----------------------------------------------------------
# Example 6 : Images Side by Side
# ----------------------------------------------------------

st.subheader("Example 6 : Images")

img1, img2 = st.columns(2)

with img1:

    st.image(
        "https://picsum.photos/300",
        caption="Image 1"
    )

with img2:

    st.image(
        "https://picsum.photos/301",
        caption="Image 2"
    )

st.divider()

# ----------------------------------------------------------
# Example 7 : Buttons Side by Side
# ----------------------------------------------------------

st.subheader("Example 7 : Buttons")

b1, b2, b3 = st.columns(3)

with b1:
    st.button("Save")

with b2:
    st.button("Update")

with b3:
    st.button("Delete")

st.divider()

# ----------------------------------------------------------
# Example 9 : Different Widgets
# ----------------------------------------------------------

st.subheader("Example 9")

c1, c2 = st.columns(2)

with c1:

    st.slider("Age",18,60)

with c2:

    st.selectbox(
        "Branch",
        ["CSE","IT","ECE"]
    )

st.divider()

# ----------------------------------------------------------
# Example 10 : Mini Dashboard
# ----------------------------------------------------------

st.subheader("Example 10 : Dashboard")

m1,m2,m3,m4 = st.columns(4)

with m1:
    st.metric("Accuracy","98%")

with m2:
    st.metric("Precision","95%")

with m3:
    st.metric("Recall","94%")

with m4:
    st.metric("F1 Score","96%")
