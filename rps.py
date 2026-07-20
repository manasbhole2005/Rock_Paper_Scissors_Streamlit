import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", layout="centered")

choices = ["Rock", "Paper", "Scissors"]

if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "ties" not in st.session_state:
    st.session_state.ties = 0

st.sidebar.title("🎮 Rock Paper Scissors")
st.sidebar.write("Play against the computer!")

st.title("🎮 Rock Paper Scissors")

user_choice = st.selectbox("Choose Your Move", choices)

col1, col2 = st.columns(2)

play = col1.button("Play", use_container_width=True)
reset = col2.button("Reset Score", use_container_width=True)

if play:

    computer_choice = random.choice(choices)

    st.subheader("Game Result")

    c1, c2 = st.columns(2)

    c1.info(f"👤 You: {user_choice}")
    c2.info(f"💻 Computer: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a Tie!"
        st.session_state.ties += 1

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = " You Win!"
        st.session_state.user_score += 1

    else:
        result = " Computer Wins!"
        st.session_state.computer_score += 1

    st.success(result)

st.divider()

st.subheader("📊 Scoreboard")

s1, s2, s3 = st.columns(3)

s1.metric("You", st.session_state.user_score)
s2.metric("Computer", st.session_state.computer_score)
s3.metric("Ties", st.session_state.ties)

if reset:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.success("Scoreboard Reset Successfully!")

st.divider()
st.caption("Developed using Python & Streamlit")
