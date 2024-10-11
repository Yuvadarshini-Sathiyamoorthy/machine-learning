import streamlit as st

# Title and Header
st.title("AI Mock Interview Website")
st.header("Welcome to the Mock Interview Portal")

# Aptitude Section
st.subheader("Aptitude Question")
st.write("What is 5 + 7?")
answer = st.radio("Choose the correct answer:", ['10', '11', '12', '13'])

# Submit Button
if st.button("Submit"):
    if answer == '12':
        st.success("Correct Answer!")
    else:
        st.error("Wrong Answer, try again!")

# Programming Section
st.subheader("Programming Question")
code_answer = st.text_area("Write a Python function to calculate the factorial of a number.")

if st.button("Submit Code"):
    if "def factorial" in code_answer:
        st.success("Good job!")
    else:
        st.error("Please write a valid function.")
    
# End of mock interview
st.write("### Thank you for participating in the mock interview.")
