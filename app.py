import streamlit as st
import pickle
import pandas as pd

# Load pipeline
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.set_page_config(page_title="IPL Win Predictor", layout="centered")

st.title("🏏 IPL Team Win Predictor")
st.write("Predict match-winning probability using Machine Learning")

teams = [
    'Mumbai Indians', 'Chennai Super Kings', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Rajasthan Royals',
    'Sunrisers Hyderabad', 'Delhi Capitals', 'Punjab Kings'
]

cities = [
    'Mumbai', 'Chennai', 'Bangalore', 'Kolkata',
    'Delhi', 'Hyderabad', 'Jaipur', 'Mohali'
]

batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", teams)
city = st.selectbox("Match City", cities)

runs_left = st.number_input("Runs Left", 0, 300, 50)
balls_left = st.number_input("Balls Left", 1, 120, 30)
wickets = st.number_input("Wickets Left", 0, 10, 5)
total_runs = st.number_input("Target Score", 50, 300, 180)

crr = st.number_input("Current Run Rate", 0.0, 20.0, 7.5)
rrr = st.number_input("Required Run Rate", 0.0, 36.0, 8.0)

if st.button("Predict Winning Probability"):
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets],
        'total_runs': [total_runs],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(input_df)

    win_prob = result[0][1] * 100
    lose_prob = result[0][0] * 100

    st.success(f"🏆 Win Probability: {win_prob:.2f}%")
    st.error(f"❌ Lose Probability: {lose_prob:.2f}%")
