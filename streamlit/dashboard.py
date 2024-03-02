import pandas as pd
import numpy as np 
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import datetime

# Dashboard
#Title

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Bike Sharing Analyze Dashboard")
st.markdown("**All the summary about data Bike Sharing, for source, see [here](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)**")
# SIDEBAR
st.sidebar.title("About me")
st.sidebar.markdown("*Dea Ramanda*")
st.sidebar.markdown(
    "**• Email: [iamadnamar@gmail.com](iamadnamar@gmail.com)**")
st.sidebar.markdown(
    "**• ID Dicoding: [senzaura](https://www.dicoding.com/users/senzaura/academies)**")
st.sidebar.markdown(
    "**• Github: [adnamard](https://github.com/adnamard)**")

#Load data
df_day = pd.read_csv("all_data.csv")
#Show Raw Data
st.subheader("Raw Data Bike Sharing")
st.write(df_day)


st.markdown("After do some analyze, here's the summary we can take from our data")
#Proyeksi perental berdasarkan bulan dan musim
# Bagian untuk grafik pertama: Proyeksi Perental Berdasarkan Bulan
fig, ax = plt.subplots(figsize=(25,5))
sns.barplot(data=df_day[['month', 'total_count']], x='month', y='total_count', ax=ax)
ax.set(title='Proyeksi Perental Berdasarkan Bulan')

st.subheader("1. Proyeksi Perental Berdasarkan Bulan")
st.pyplot(fig)  # Menampilkan grafik pertama di Streamlit

# Bagian untuk grafik kedua: Proyeksi Perental Berdasarkan Musim
plt.figure(figsize=(10, 5))
sns.pointplot(data=df_day, x='month', y='total_count', hue='season', palette='coolwarm', markers=["o", "x", "s", "D"], linestyles=["-", "--", "-.", ":"])
plt.title('Proyeksi Perental per Bulan Berdasarkan Musim')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewa')
plt.xticks(ticks=range(0, 12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
plt.grid(True)
# Karena plt.figure() membuat figur baru, kita tidak perlu menentukan axis seperti pada grafik pertama

st.subheader("2. Proyeksi Perental Berdasarkan Musim")
st.pyplot()  # Menampilkan grafik kedua di Streamlit

#TAMPILIH 4 VARIABLE

st.subheader("3. Proyeksi Hubungan dengan Perental Berdasarkan Beberapa Variabel")
col1, col2 = st.columns(2)

# Grafik pertama: Hubungan Kelembapan/Humidity dengan Jumlah Perental
with col1:
    fig, ax = plt.subplots()
    sns.regplot(x='humidity', y='total_count', data=df_day, scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
    ax.set(title='Proyeksi Hubungan Kelembapan/Humidity dengan Jumlah Perental')
    st.caption("A. Proyeksi Hubungan Kelembapan/Humidity dengan Jumlah Perental")
    st.pyplot(fig)

# Grafik kedua: Hubungan Suhu/Temperature dengan Jumlah Perental
with col2:
    fig, ax = plt.subplots()
    sns.regplot(x='temp', y='total_count', data=df_day, scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
    ax.set(title='Proyeksi Hubungan Suhu/Temperature dengan Jumlah Perental')
    st.caption("B. Proyeksi Hubungan Suhu/Temperature dengan Jumlah Perental")
    st.pyplot(fig)

col1, col2 = st.columns(2)

# Grafik Ketiga: Hubungan Kondisi Cuaca dengan Jumlah Perental
with col1:
    fig, ax = plt.subplots()
    # Jika 'weather_condi' adalah numerik dan merepresentasikan kategori, gunakan barplot
    sns.barplot(x='weather_condi', y='total_count', data=df_day, ax=ax)
    ax.set(title='Proyeksi Hubungan Cuaca/Weather dengan Jumlah Perental')
    st.caption("C. Proyeksi Hubungan Cuaca/Weather dengan Jumlah Perental")
    st.pyplot(fig)
    with st.expander("See explanation"):
        st.caption("1=clear, 2=Mist, 3=Light Snow, 4=Heavy Rain")

# Grafik Keempat: Hubungan Kecepatan Angin dengan Jumlah Perental
with col2:
    fig, ax = plt.subplots()
    sns.regplot(x='windspeed', y='total_count', data=df_day, scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
    ax.set(title='Proyeksi Hubungan Kecepatan Angin/Windspeed dengan Jumlah Perental')
    st.caption("D. Proyeksi Hubungan Kecepatan Angin/Windspeed dengan Jumlah Perental")
    st.pyplot(fig)

st.subheader("4. Perbandingan Jumlah Total Keseluruhan Penyewaan Sepeda pada Summer dan Winter (2011 vs 2012)")
# Data untuk plot
filtered_data1 = df_day[(df_day["year"] == 0) & (df_day["season"] == 2)]
filtered_data2 = df_day[(df_day["year"] == 1) & (df_day["season"] == 2)]
filtered_data3 = df_day[(df_day["year"] == 0) & (df_day["season"] == 4)]
filtered_data4 = df_day[(df_day["year"] == 1) & (df_day["season"] == 4)]

summer1 = filtered_data1["total_count"].sum()
summer2 = filtered_data2["total_count"].sum()
winter1 = filtered_data3["total_count"].sum()
winter2 = filtered_data4["total_count"].sum()
print("Perbandingan jumlah total keseluruhan perental sepeda pada tiap summer dan winter")
print(f"summer 2011: {summer1}")
print(f"summer 2012: {summer2}")
print(f"winter 2011: {winter1}")
print(f"winter 2012: {winter2}")
print(f"Selisih winter: {winter2-winter1}")
print(f"Selisih summer: {summer2-summer1}")
years = ['Summer 2011', 'Summer 2012', 'Winter 2011', 'Winter 2012']
totals = [summer1, summer2, winter1, winter2]
years = ['Summer 2011', 'Summer 2012', 'Winter 2011', 'Winter 2012']
totals = [summer1, summer2, winter1, winter2]

# Membuat figure dan ax menggunakan Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(years, totals, color=['grey', 'lightblue', 'grey', 'lightblue'])

# Menambahkan judul dan label
ax.set_title('5. Perbandingan Jumlah Total Keseluruhan Penyewaan Sepeda pada Summer dan Winter (2011 vs 2012)')
ax.set_xlabel('Musim dan Tahun')
ax.set_ylabel('Jumlah Total Penyewaan')

# Menampilkan nilai di atas tiap bar
for i, total in enumerate(totals):
    ax.text(i, total + 500, str(total), ha='center')

# Menampilkan plot di Streamlit
st.pyplot(fig)
with st.expander("See explanation"):
    st.write("Dapat disimpulkan bahwa terjadi kenaikan perental sepeda baik di masing masing musim summer dan winter. Kenaikan tersebut mencapai 189339 untuk musim winter 2011-2012, dan mencapai 223957 untuk musim summer 2011-2012")





st.subheader("Perbandingan jumlah perental sepeda yang terdaftar pada tiap summer dan winter di tahun 2012")


filtered_data1= df_day[(df_day["year"] == 1) & (df_day["season"] == 2) & (df_day["is_workingday"] == 1)]
filtered_data2= df_day[(df_day["year"] == 1) & (df_day["season"] == 4) & (df_day["is_workingday"] == 1)]
summer = filtered_data1["registered"].sum()
winter = filtered_data2["registered"].sum()
print("Perbandingan jumlah perental sepeda yang terdaftar pada tiap summer dan winter di tahun 2012")
print(f"Summer 2012: {summer}")
print(f"Winter 2012: {winter}")
print(f"Selisih    : {summer - winter}")

# Data
categories = ['Summer 2012', 'Winter 2012']
values = [summer, winter]


# Membuat bar chart
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(categories, values, color=['lightblue', 'grey'])

# Menambahkan judul dan label
ax.set_title('Perbandingan Jumlah Penyewa Sepeda yang Terdaftar pada Summer dan Winter di Tahun 2012')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Penyewa Terdaftar')

# Menambahkan nilai di atas bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 500, int(height), ha='center', va='bottom')

# Menampilkan plot di Streamlit
st.pyplot(fig)
with st.expander("See explanation"):
    st.write("Dapat disimpulkan bahwa perental yang sudah terdaftar yang merental pada hari kerja tidak terlalu terjadi perubahan yang signifikan baik dalam musim panas/summer maupun musim dingin/winter di tahun 2012, hal ini dibuktikan dengan selisih perbedaan jumlah perental terdaftar dari di summer dan winter pada thaun 2012 sebesar: 9629 perental.")


st.caption('Copyright (c) Adnamar 2023')
