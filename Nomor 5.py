import streamlit as st
from datetime import datetime, date, time

# Number input
st.number_input("Pick a number", min_value=0, max_value=100, value=1, step=1)

# Email input
st.text_input("Email adress")

# Date input
st.date_input("Travelling date", value=date(2022, 6, 17))

# Time input
st.time_input("School time", value=time(8, 0))

# Multiline text area
st.text_area("Description")

# File uploader
st.file_uploader("Upload a photo", type=["jpg", "png", "jpeg"])

# Color picker
st.color_picker("Choose your favourite color", value="#ff00ff")