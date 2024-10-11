import streamlit as st
import requests

# Set custom CSS for colors, fonts, and styles
st.markdown("""
    <style>
    body {
        background-color: #1c1c1c;
        color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #ff69b4;
        font-size: 50px;
        font-weight: bold;
    }
    .subheader {
        color: #ff1493;
        font-size: 36px;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #ff69b4;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #ff1493;
        color: white;
    }
    .stRadio>div>div {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Mock Interview Navigation")
pages = ["MCQ Round", "Coding Round", "Communication Round"]
page = st.sidebar.radio("Go to", pages)

# Fetch random MCQs from Open Trivia DB API
def get_random_mcq():
    url = "https://opentdb.com/api.php?amount=1&type=multiple"
    response = requests.get(url).json()
    question_data = response['results'][0]
    question = question_data['question']
    correct_answer = question_data['correct_answer']
    incorrect_answers = question_data['incorrect_answers']
    return question, correct_answer, incorrect_answers

# Function for AI feedback
def generate_feedback(score):
    if score > 80:
        return "Excellent performance! Keep up the great work!"
    elif score > 50:
        return "Good job! But there's room for improvement."
    else:
        return "You need to work harder. Review the basics and try again."

# MCQ Round
if page == "MCQ Round":
    st.markdown('<p class="title">Multiple Choice Questions (MCQ)</p>', unsafe_allow_html=True)
    question, correct_answer, incorrect_answers = get_random_mcq()
    answers = incorrect_answers + [correct_answer]
    st.markdown(f"<p class='subheader'>{question}</p>", unsafe_allow_html=True)
    user_answer = st.radio("Choose your answer:", answers)
    
    if st.button("Submit Answer"):
        if user_answer == correct_answer:
            st.success("Correct!")
        else:
            st.error(f"Incorrect! The correct answer was {correct_answer}.")

# Coding Round
elif page == "Coding Round":
    st.markdown('<p class="title">Coding Challenge</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">Write a Python function to reverse a string.</p>', unsafe_allow_html=True)
    
    code_answer = st.text_area("Write your code below:")
    
    if st.button("Run Code"):
        if "def reverse_string" in code_answer:
            st.success("Good code structure!")
        else:
            st.error("Try again! Make sure to define the function properly.")
    
    # AI Feedback
    st.markdown('<p class="subheader">AI Feedback</p>', unsafe_allow_html=True)
    score = 70  # Example score based on some criteria
    st.write(generate_feedback(score))

# Communication Round
elif page == "Communication Round":
    st.markdown('<p class="title">Communication Practice</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">Practice a short introduction for an interview.</p>', unsafe_allow_html=True)
    
    intro = st.text_area("Introduce yourself:")
    
    if st.button("Submit"):
        st.write("Thank you for your introduction!")
        
        # Simple AI analysis (just a placeholder)
        if len(intro.split()) > 30:
            st.success("Great introduction! You explained well.")
        else:
            st.warning("Your introduction is too short. Try to add more details.")

    # Communication tips
    st.markdown('<p class="subheader">AI Communication Tips</p>', unsafe_allow_html=True)
    st.write("Tip: Speak clearly and confidently, and maintain good body language.")

# Footer
st.sidebar.write("### Powered by AI Mock Interview Platform")
