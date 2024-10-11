import streamlit as st
from PIL import Image

# Set background color and font style using custom CSS
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Helvetica', sans-serif;
    }
    .title {
        color: #4a4a4a;
        font-size: 50px;
        font-weight: bold;
    }
    .header {
        color: #2e8b57;
        font-size: 36px;
        font-weight: bold;
    }
    .subheader {
        color: #d2691e;
        font-size: 28px;
    }
    .question-text {
        font-size: 20px;
        font-weight: bold;
    }
    .stRadio {
        color: #333;
        background-color: #fff;
    }
    .stButton>button {
        background-color: #008cba;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #005f73;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Header
st.markdown('<p class="title">AI Mock Interview Website</p>', unsafe_allow_html=True)
st.markdown('<p class="header">Welcome to the Mock Interview Portal</p>', unsafe_allow_html=True)

# Optional: Add an image (can be replaced by your image)
st.image('https://via.placeholder.com/400x100', caption='Interview Simulation', use_column_width=True)

# Aptitude Section
st.markdown('<p class="subheader">Aptitude Question</p>', unsafe_allow_html=True)
st.markdown('<p class="question-text">What is 5 + 7?</p>', unsafe_allow_html=True)
answer = st.radio("", ['10', '11', '12', '13'])

# Submit Button
if st.button("Submit Answer"):
    if answer == '12':
        st.success("🎉 Correct Answer!")
    else:
        st.error("❌ Wrong Answer, try again!")

# Programming Section
st.markdown('<p class="subheader">Programming Question</p>', unsafe_allow_html=True)
code_answer = st.text_area("Write a Python function to calculate the factorial of a number.")

if st.button("Submit Code"):
    if "def factorial" in code_answer:
        st.success("🎉 Good job!")
    else:
        st.error("❌ Please write a valid function.")

# End of mock interview
st.write("### Thank you for participating in the mock interview.")
