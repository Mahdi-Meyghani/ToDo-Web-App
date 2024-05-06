import streamlit as st
import time
import moods_functions

today = time.strftime("%Y/%m/%d")
rating_list = moods_function.get_moods()


def rate_mood():
    if st.session_state["mood"]:
        new_mood = f"Your mood at {today} is: {st.session_state['mood']}\n"
        rating_list.insert(0, new_mood)
        moods_function.write_moods(rating_list)
    for i in rating_list:
        st.write(i)


st.text_input(label="How do you rate your mood today from 1 to 10 ?",
              placeholder="Rate your mood", key="mood")

rate_mood()
