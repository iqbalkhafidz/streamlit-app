import streamlit as st

# Checkbox
st.checkbox("yes")

# Button
st.button("Click")

# Radio button
st.radio("Pick your gender", ["Male", "Female"])

# Selectbox (dropdown)
st.selectbox("Pick your gender", ["Male", "Female"])

# Selectbox dengan placeholder
st.selectbox("choose a planet", ["Choose an option"])

# Slider dengan label (gunakan label tambahan secara manual)
st.markdown("Pick a mark")
mark = st.slider("", 0, 100, 50)
st.markdown(f"<div style='display: flex; justify-content: space-between; color: red;'>"
            f"<span>Bad</span><span style='margin-left: auto;'>Good</span><span style='margin-left: auto;'>Excellent</span></div>", unsafe_allow_html=True)

# Slider angka biasa
st.markdown("Pick a number")
st.slider("", 0, 10, 9)