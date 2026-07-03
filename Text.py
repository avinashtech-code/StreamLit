import streamlit as st

# ======================================
# TITLE
# ======================================

st.title(" Streamlit Text Elements Demo")

# ======================================
# HEADER
# ======================================

st.header(" Header Example")

# ======================================
# SUBHEADER
# ======================================

st.subheader("This is a Subheader")

# ======================================
# WRITE
# ======================================

st.header("st.write() Examples")

st.write("Hello World")
st.write(100)
st.write(99.99)
st.write(True)

name = "Avinash"
age = 20

st.write("Name:", name)
st.write("Age:", age)

st.write(["Python", "Java", "C++"])

st.write(("Apple", "Mango", "Banana"))

st.write({"Python", "Java", "C++"})

st.write({
    "Name": "Avinash",
    "College": "NSUT",
    "Age": 20
})

# ======================================
# TEXT
# ======================================

st.header("st.text() Examples")

st.text("This is plain text.")

# ======================================
# MARKDOWN
# ======================================

st.header("st.markdown() Examples")

# Headings
st.markdown("# Heading 1")
st.markdown("## Heading 2")
st.markdown("### Heading 3")
st.markdown("#### Heading 4")
st.markdown("##### Heading 5")
st.markdown("###### Heading 6")

# Bold
st.markdown("**Bold Text**")

# Italic
st.markdown("*Italic Text*")

# Bold + Italic
st.markdown("***Bold + Italic***")

# Block Quote
st.markdown("> This is a block quote.")

# Code Block
st.markdown("""
```python
for i in range(5):
    print(i)
```
""")

# Bullet List
st.markdown("""
- Python
- Java
- C++
- JavaScript
""")

# Numbered List
st.markdown("""
1. Apple
2. Mango
3. Banana
""")

# Task List
st.markdown("""
- [x] Learn Python
- [x] Learn ML
- [ ] Learn GenAI
""")

# Table
st.markdown("""
| Name | Age |
|------|-----|
| Avinash | 20 |
| Rahul | 21 |
""")

# Hyperlink
st.markdown("[Open Google](https://www.google.com)")

# Image
st.markdown("![Python Logo](https://www.python.org/static/community_logos/python-logo.png)")

# ======================================
# CAPTION
# ======================================

st.header("st.caption() Examples")

st.caption("This is a caption.")
st.caption("Version 1.0.0")


# ======================================
# LATEX
# ======================================

st.header("st.latex() Examples")
st.latex(r"E = mc^2")
st.latex(r"\frac{a}{b}")
st.latex(r"\sqrt{x}")
st.latex(r"x^2+y^2=z^2")
st.latex(r"\sum_{i=1}^{n} i")
st.latex(r"\int_0^1 x^2 dx")
st.latex(r"\lim_{x\to0}\frac{\sin x}{x}")
st.latex(r"\alpha + \beta = \gamma")
st.latex(r"\theta = \frac{\pi}{4}")
st.latex(r"\sigma = \sqrt{\frac{1}{N}\sum (x-\mu)^2}")
# ======================================
# DIVIDER
# ======================================
st.header("st.divider() Examples")
st.write("Section 1")
st.divider()
st.write("Section 2")
st.divider()
st.write("Section 3")
st.divider()
st.write("End of Demo ")
