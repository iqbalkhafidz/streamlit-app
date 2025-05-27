import streamlit as st

st.title("this is the app title")
st.markdown("this is the markdown")
st.header("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")

x = 2021
st.code(f"x={x}", language='python')