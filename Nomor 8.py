import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Aplikasi Iklim: Data Suhu & Curah Hujan")

# Sidebar menu
menu = st.sidebar.selectbox("Pilih Menu", ["Home", "Gambar", "Dataset", "Grafik"])

# Baca dataset
df = pd.read_csv("datacuaca.csv")

if menu == "Home":
    st.subheader("Menampilkan Gambar")
    st.image("gambar.jpg", caption="Contoh Gambar", use_container_width=True)

    st.subheader("Menampilkan Dataset Iklim")
    st.dataframe(df)

    st.subheader("Grafik Suhu dan Curah Hujan")
    fig, ax = plt.subplots()
    ax.plot(df['Month'], df['Temperature '], marker='o', label='Suhu')
    ax.plot(df['Month'], df['Rain'], marker='s', label='Curah Hujan')
    ax.set_title("Suhu & Curah Hujan Bulanan (Tahun 1901)")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Nilai")
    ax.legend()
    st.pyplot(fig)

elif menu == "Gambar":
    st.subheader("Menampilkan Gambar")
    st.image("gambar.jpg", caption="Contoh Gambar", use_container_width=True)

elif menu == "Dataset":
    st.subheader("Menampilkan Dataset Iklim")
    st.dataframe(df)

elif menu == "Grafik":
    st.subheader("Grafik Suhu dan Curah Hujan")
    fig, ax = plt.subplots()
    ax.plot(df['Month'], df['Temperature '], marker='o', label='Suhu')
    ax.plot(df['Month'], df['Rain'], marker='s', label='Curah Hujan')
    ax.set_title("Suhu & Curah Hujan Bulanan (Tahun 1901)")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Nilai")
    ax.legend()
    st.pyplot(fig)
