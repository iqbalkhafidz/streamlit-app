import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load dataset
df = pd.read_csv('CarPrice.csv')

# Load model
model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))

# Judul
st.title("Prediksi Harga Mobil")

# Tampilkan dataset
st.subheader("Dataset")
st.dataframe(df)

# Grafik horsepower
st.subheader("Grafik Horsepower")
st.line_chart(df['horsepower'])

# Grafik curbweight
st.subheader("Grafik Curbweight")
st.line_chart(df['curbweight'])

# Grafik enginesize
st.subheader("Grafik Enginesize")
st.line_chart(df['enginesize'])

# Input pengguna
st.subheader("Input Fitur")

horsepower = st.selectbox("Horsepower", sorted(df['horsepower'].unique()))
curbweight = st.selectbox("Curb Weight", sorted(df['curbweight'].unique()))
enginesize = st.selectbox("Engine Size", sorted(df['enginesize'].unique()))
highwaympg = st.selectbox("Highway MPG", sorted(df['highwaympg'].unique()))

# Prediksi
if st.button("Prediksi"):
    input_data = np.array([[horsepower, curbweight, enginesize, highwaympg]])
    prediksi_harga = model.predict(input_data)
    st.success(f"Prediksi harga mobil: ${prediksi_harga[0]:,.2f}")