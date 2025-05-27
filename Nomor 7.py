import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y']
)

st.subheader("Line Chart")
st.line_chart(df)


st.subheader("Bar Chart")
st.bar_chart(df)

st.subheader("Area Chart")
st.area_chart(df)