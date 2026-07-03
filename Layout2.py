import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Layout Part 2", layout="wide")

st.title("📐 Module 7 - Layout (Part 2)")

# ============================================================
# SAMPLE DATA
# ============================================================

df = pd.DataFrame({
    "Name": ["Avinash", "Rahul", "Priya"],
    "Age": [20, 21, 22],
    "CGPA": [8.9, 8.5, 9.2]
})

# ============================================================
# st.tabs()
# ============================================================

st.header("1. st.tabs()")

# ------------------------------------------------------------
# Example 1 : Basic Tabs
# ------------------------------------------------------------

tab1, tab2, tab3 = st.tabs(["🏠 Home", "👤 Profile", "⚙️ Settings"])

with tab1:
    st.write("Welcome to Home Page")

with tab2:
    st.write("This is Profile Page")

with tab3:
    st.write("This is Settings Page")

st.divider()

# ------------------------------------------------------------
# Example 2 : Forms Inside Tabs
# ------------------------------------------------------------

st.subheader("Example 2")

login, signup = st.tabs(["Login", "Signup"])

with login:
    st.text_input("Username")
    st.text_input("Password", type="password")
    st.button("Login")

with signup:
    st.text_input("Full Name")
    st.text_input("Email")
    st.text_input("Create Password", type="password")
    st.button("Signup")

st.divider()

# ------------------------------------------------------------
# Example 3 : Data Inside Tabs
# ------------------------------------------------------------

st.subheader("Example 3")

table_tab, json_tab = st.tabs(["Table", "JSON"])

with table_tab:
    st.dataframe(df)

with json_tab:
    st.json(df.to_dict())

st.divider()

# ------------------------------------------------------------
# Example 4 : Media Inside Tabs
# ------------------------------------------------------------

st.subheader("Example 4")

image_tab, video_tab = st.tabs(["Image", "Video"])

with image_tab:
    st.image("https://picsum.photos/500")

with video_tab:
    st.video(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    )

st.divider()

# ------------------------------------------------------------
# Example 5 : Dashboard Tabs
# ------------------------------------------------------------

st.subheader("Example 5")

overview, analytics, reports = st.tabs(
    ["Overview", "Analytics", "Reports"]
)

with overview:
    st.metric("Users", "2500", "+150")

with analytics:
    st.bar_chart(df.set_index("Name")["CGPA"])

with reports:
    st.success("Report Generated Successfully")

# ============================================================
# st.expander()
# ============================================================

st.header("2. st.expander()")

# Example 1

with st.expander("Student Details"):
    st.write("Name : Avinash")
    st.write("College : NSUT")
    st.write("Branch : CSE")

# Example 2

with st.expander("Show Table"):
    st.dataframe(df)

# Example 3

with st.expander("Show JSON"):
    st.json(df.to_dict())

# Example 4

with st.expander("Advanced Settings"):
    st.slider("Learning Rate", 1, 100)
    st.checkbox("Enable GPU")
    st.selectbox("Optimizer", ["Adam", "SGD"])

# Example 5

with st.expander("FAQ"):

    st.write("Q. What is Streamlit?")
    st.write("A. A Python framework for web apps.")

st.divider()

# ============================================================
# st.container()
# ============================================================

st.header("3. st.container()")

# Example 1

st.subheader("Example 1")

with st.container():
    st.success("Container Started")
    st.write("Everything here belongs to one section.")

st.divider()

# Example 2

st.subheader("Example 2")

with st.container():
    st.text_input("Name")
    st.number_input("Age")
    st.button("Submit")

st.divider()

# Example 3

st.subheader("Example 3")

with st.container():
    st.metric("Accuracy", "98%")
    st.metric("Precision", "95%")

st.divider()

# Example 4

st.subheader("Example 4")

with st.container():
    st.dataframe(df)
    st.bar_chart(df.set_index("Name")["CGPA"])

st.divider()

# Example 5

st.subheader("Example 5")

container = st.container()

with container:
    st.header("Dashboard Section")
    st.write("Revenue : ₹50,000")
    st.write("Orders : 520")

st.divider()

# ============================================================
# st.empty()
# ============================================================

st.header("4. st.empty()")

# Example 1 : Replace Text

placeholder = st.empty()

placeholder.info("Loading...")

if st.button("Replace Text"):
    placeholder.success("Loaded Successfully")

st.divider()

# Example 2 : Replace with DataFrame

placeholder2 = st.empty()

if st.button("Show DataFrame"):
    placeholder2.dataframe(df)

st.divider()

# Example 3 : Replace with Chart

placeholder3 = st.empty()

if st.button("Show Chart"):
    placeholder3.bar_chart(df.set_index("Name")["CGPA"])

st.divider()

# Example 4 : Progress Simulation

placeholder4 = st.empty()

if st.button("Start Process"):

    placeholder4.warning("Processing...")

    time.sleep(2)

    placeholder4.success("Completed Successfully")

st.divider()

# Example 5 : Dynamic Messages

placeholder5 = st.empty()

if st.button("Change Message"):

    placeholder5.write("First Message")

    time.sleep(1)

    placeholder5.write("Second Message")

    time.sleep(1)

    placeholder5.success("Done ✅")
