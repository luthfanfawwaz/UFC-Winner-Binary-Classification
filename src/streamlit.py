import streamlit as st
import requests
from PIL import Image

# Load and set images in the first place
header_images = Image.open('assets/ufc-logo.jpeg')
st.image(header_images)

# Add some information about the service
st.title("UFC Winner Prediction")
st.subheader("You can enter the following variables then click Predict button to see who's better :punch:")

# Create form of input
with st.form(key = "ufc_winner_prediction"):
    # Create columns for each fighter
    red_col, blue_col = st.columns(2)
    # Red fighter column
    with red_col:
        red_win = st.number_input(
            label = "Number of :red[Red] fighter's Win:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        red_loss = st.number_input(
            label = "Number of :red[Red] fighter's Loss:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        red_win_streak = st.number_input(
            label = "Number of :red[Red] fighter's Win Streak:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        red_lose_streak = st.number_input(
            label = "Number of :red[Red] fighter's Lose Streak:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        red_longest_win_streak = st.number_input(
            label = "Number of :red[Red] fighter's Longest Win Streak:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        red_total_round = st.number_input(
            label = "Number of :red[Red] fighter's Total Round:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        red_total_title_bout = st.number_input(
            label = "Number of :red[Red] fighter's Total Title Bout:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        red_ko = st.number_input(
            label = "Number of :red[Red] fighter's KO:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        red_sub = st.number_input(
            label = "Number of :red[Red] fighter's Win by Submission:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        red_height = st.number_input(
            label = ":red[Red] fighter's Height:",
            min_value = 0,
            help = "The number cannot go below 0. Unit in centimeters."
            )

        red_reach = st.number_input(
            label = ":red[Red] fighter's Reach:",
            min_value = 0,
            help = "The number cannot go below 0. Unit in centimeters."
            )

        red_age = st.number_input(
            label = ":red[Red] fighter's Age:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

    # Blue fighter column
    with blue_col:
        # Create box for number input
        blue_win = st.number_input(
            label = "Number of :blue[Blue] fighter's Win:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        blue_loss = st.number_input(
            label = "Number of :blue[Blue] fighter's Loss:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        blue_win_streak = st.number_input(
            label = "Number of :blue[Blue] fighter's Win Streak:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        blue_lose_streak = st.number_input(
            label = "Number of :blue[Blue] fighter's Lose Streak:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        blue_longest_win_streak = st.number_input(
            label = "Number of :blue[Blue] fighter's Longest Win Streak:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        blue_total_round = st.number_input(
            label = "Number of :blue[Blue] fighter's Total Round:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        blue_total_title_bout = st.number_input(
            label = "Number of :blue[Blue] fighter's Total Title Bout:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        blue_ko = st.number_input(
            label = "Number of :blue[Blue] fighter's KO:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        blue_sub = st.number_input(
            label = "Number of :blue[Blue] fighter's Win by Submission:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

        blue_height = st.number_input(
            label = ":blue[Blue] fighter's Height:",
            min_value = 0,
            help = "The number cannot go below 0. Unit in centimeters."
            )

        blue_reach = st.number_input(
            label = ":blue[Blue] fighter's Reach:",
            min_value = 0,
            help = "The number cannot go below 0. Unit in centimeters."
            )

        blue_age = st.number_input(
            label = ":blue[Blue] fighter's Age:",
            min_value = 0,
            help = "The number cannot go below 0."
            )

    # Create button to submit the form
    submitted = st.form_submit_button("Predict")

    # Condition when form submitted
    if submitted:
        # Create dict of all data in the form
        raw_data = {
            "lose_streak_dif": red_lose_streak - blue_lose_streak,
            "win_streak_dif": red_win_streak - blue_win_streak,
            "longest_win_streak_dif": red_longest_win_streak - blue_longest_win_streak,
            "win_dif": red_win - blue_win,
            "loss_dif": red_loss - blue_loss,
            "total_round_dif": red_total_round - blue_total_round,
            "total_title_bout_dif": red_total_title_bout - blue_total_title_bout,
            "ko_dif": red_ko - blue_ko,
            "sub_dif": red_sub - blue_sub,
            "height_dif": red_height - blue_height,
            "reach_dif": red_reach - blue_reach,
            "age_dif": red_age - blue_age
        }

        # Create loading animation while predicting
        with st.spinner("Sending data to prediction server ..."):
            res = requests.post("http://fastapi_be:8080/predict", json = raw_data).json()
            
        # Parse the prediction result
        if res["error_msg"] != "":
            st.error("Error Occurs While Predicting: {}".format(res["error_msg"]))
        else:
            if res["res"] == "Biru Menang.":
                st.balloons()
                st.info("Blue Fighter Wins")
            else:
                st.balloons()
                st.error("Red Fighter Wins")