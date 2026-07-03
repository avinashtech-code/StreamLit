import streamlit as st

st.title("st.text_input() Demo")

# 1. Simple Text Input
name = st.text_input("Enter your Name")
st.write("Name:", name)

# 2. Default Value
default_name = st.text_input(
    "Default Name",
    value="Avinash"
)
st.write("Default Name:", default_name)

# 3. Email Input
email = st.text_input(
    "Email",
    placeholder="example@gmail.com"
)
st.write("Email:", email)

# 4. Password Input
password = st.text_input(
    "Password",
    type="password"
)
st.write("Password Length:", len(password))

# 5. API Key
api_key = st.text_input(
    "OpenAI API Key",
    type="password"
)
st.write("API Key Length:", len(api_key))

# 6. Disabled Input
st.text_input(
    "Disabled Field",
    value="Avinash",
    disabled=True
)

# 7. Search Bar
search = st.text_input(
    "Search",
    placeholder="Search products..."
)
st.write("Searching:", search)

# 8. Website URL
url = st.text_input(
    "Website URL",
    placeholder="https://example.com"
)
st.write("URL:", url)

# 9. OTP
otp = st.text_input(
    "OTP",
    max_chars=6
)
st.write("OTP:", otp)

# 10. Help + Icon
city = st.text_input(
    "City",
    placeholder="Enter your city",
    help="Type your current city",
    icon="🏙️"
)
st.write("City:", city)
