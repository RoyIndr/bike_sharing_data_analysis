import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import streamlit as st 
sns.set(style="white")

def create_eleven_day_df(df):
    return df.drop(df[df["yr"]==1].index)

def create_twelve_day_df(df):
    return df.drop(df[df["yr"]==0].index)

def create_monthly_users_day_df(df):
    monthly_users_day_df = df.resample(rule='D', on="dteday").agg({
        "cnt": "sum"
    })
    monthly_users_day_df = monthly_users_day_df.reset_index()
    
    return monthly_users_day_df

def create_monthly_users_eleven_day_df(df):
    eleven_day_df = create_eleven_day_df(df)
    
    monthly_users_eleven_day_df = eleven_day_df.resample(rule='M', on="dteday").agg({
        "cnt": "sum"
    })
    monthly_users_eleven_day_df = monthly_users_eleven_day_df.reset_index()
    
    return monthly_users_eleven_day_df
    
def create_season_users_eleven_day_df(df):
    eleven_day_df = create_eleven_day_df(df)
    
    season_users_eleven_day_df = eleven_day_df.groupby(by="season").agg({
        "cnt": "sum"
    }).reset_index()
    season_users_eleven_day_df.replace([1, 2, 3, 4], ['spring', 'summer', 'autumn', 'winter'], inplace=True)
    
    return season_users_eleven_day_df

def create_weather_users_eleven_day_df(df):
    eleven_day_df = create_eleven_day_df(df)
    
    weather_users_eleven_day_df = eleven_day_df.groupby(by="weathersit").agg({
        "cnt": "sum"  
    }).reset_index()
    weather_users_eleven_day_df.replace([1, 2, 3, 4], ['clear', 'mist', 'slightly bad', 'very bad'], inplace=True)
    
    return weather_users_eleven_day_df

def create_monthly_users_twelve_day_df(df):
    twelve_day_df = create_twelve_day_df(df)
    
    monthly_users_twelve_day_df = twelve_day_df.resample(rule='M', on="dteday").agg({
        "cnt": "sum"
    })
    monthly_users_twelve_day_df = monthly_users_twelve_day_df.reset_index()
    
    return monthly_users_twelve_day_df
    
def create_season_users_twelve_day_df(df):
    twelve_day_df = create_twelve_day_df(df)
    
    season_users_twelve_day_df = twelve_day_df.groupby(by="season").agg({
        "cnt": "sum"
    }).reset_index()
    season_users_twelve_day_df.replace([1, 2, 3, 4], ['spring', 'summer', 'autumn', 'winter'], inplace=True)
    
    return season_users_twelve_day_df

def create_weather_users_twelve_day_df(df):
    twelve_day_df = create_twelve_day_df(df)
    
    weather_users_twelve_day_df = twelve_day_df.groupby(by="weathersit").agg({
        "cnt": "sum"
    }).reset_index()
    weather_users_twelve_day_df.replace([1, 2, 3, 4], ['spring', 'summer', 'autumn', 'winter'], inplace=True)
    
    return weather_users_twelve_day_df

#Membaca file new_day_csv
new_day_df = pd.read_csv("new_day.csv")

#Mengubah kolom dteday menjadi berformat datetime
new_day_df["dteday"] = pd.to_datetime(new_day_df["dteday"])

#Mencari tanggal terlama dan terbaru
min_date = new_day_df["dteday"].min()
max_date = new_day_df["dteday"].max()

st.header("Bike Rental Dashboard")

with st.sidebar:
    #Mengambil start_date dan end_date dari date_input
    start_date, end_date = st.date_input(
        label= "Rentang Waktu",
        min_value= min_date,
        max_value= max_date,
        value=[min_date, max_date]
    )

#Membuat dataframe main    
main_df = new_day_df[(new_day_df["dteday"] >= str(start_date)) & (new_day_df["dteday"] <= str(end_date))]

monthly_users_day_df = create_monthly_users_day_df(main_df)
monthly_users_eleven_day_df = create_monthly_users_eleven_day_df(new_day_df)
season_users_eleven_day_df = create_season_users_eleven_day_df(new_day_df)
weather_users_eleven_day_df = create_weather_users_eleven_day_df(new_day_df)
monthly_users_twelve_day_df = create_monthly_users_twelve_day_df(new_day_df)
season_users_twelve_day_df = create_season_users_twelve_day_df(new_day_df)
weather_users_twelve_day_df = create_weather_users_twelve_day_df(new_day_df)

st.subheader('Daily Users')
 
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_users = monthly_users_day_df.cnt.sum()
    st.metric("Total Users", value=total_users)
with col2:
    max_users = monthly_users_day_df.cnt.max()
    st.metric("Highest Users record", value=max_users)
with col3:
    min_users = monthly_users_day_df.cnt.min()
    st.metric("Lowest Users Record", value=min_users)
with col4:
    mean_users = monthly_users_day_df.cnt.mean()
    st.metric("Average Users Record", value=mean_users)

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(30, 10))

sns.lineplot(x="dteday", y="cnt", data=monthly_users_day_df, orient='x', ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title("Jumlah User per Bulan", loc="center", fontsize=17)
ax.tick_params(axis ='y', labelsize=12)

st.pyplot(fig)


st.subheader("Total users in 2011")

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    total_eleven_users = monthly_users_eleven_day_df.cnt.sum()
    st.metric("Total Users", value=total_eleven_users)
with col2:
    max_eleven_users = monthly_users_eleven_day_df.cnt.max()
    st.metric("Highest Users record", value=max_eleven_users)
with col3:
    min_eleven_users = monthly_users_eleven_day_df.cnt.min()
    st.metric("Lowest Users Record", value=min_eleven_users)
with col4:
    mean_eleven_users = monthly_users_eleven_day_df.cnt.mean()
    st.metric("Average Users Record", value=mean_eleven_users)

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(30, 10))

sns.lineplot(x="dteday", y="cnt", data=monthly_users_eleven_day_df, orient='x', ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_title("Jumlah User per Bulan Tahun 2011", loc="center", fontsize=17)
ax.tick_params(axis ='y', labelsize=12)

st.pyplot(fig)


col1, col2, col3, col4 = st.columns(4)
 
with col1:
    st.metric("Highest Users Season: ", value="Fall")
with col2:
    fall_users = season_users_eleven_day_df.cnt.max()
    st.metric("Fall Users Record: ", value=fall_users)
with col3:
    st.metric("Highest Users Weather: ", value="Mist")
with col4:
    mist_users = weather_users_eleven_day_df.cnt.max()
    st.metric("Mist Users Record: ", value=mist_users)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(30, 10))

season_colors = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
weather_colors = ["#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="season", y="cnt", data=season_users_eleven_day_df,palette=season_colors, hue='season', ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Jumlah User per Musim Tahun 2011", loc="center", fontsize=17)
ax[0].tick_params(axis ='y', labelsize=12)

sns.barplot(x="weathersit", y="cnt", data=weather_users_eleven_day_df, palette=weather_colors,hue='weathersit', ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].set_title("Jumlah User Pada Tiap Cuaca di Tahun 2011", loc="center", fontsize=17)
ax[1].tick_params(axis ='y', labelsize=12)

st.pyplot(fig)


st.subheader("Total users in 2012")

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    total_twelve_users = monthly_users_twelve_day_df.cnt.sum()
    st.metric("Total Users", value=total_twelve_users)
with col2:
    max_twelve_users = monthly_users_twelve_day_df.cnt.max()
    st.metric("Highest Users record", value=max_twelve_users)
with col3:
    min_twelve_users = monthly_users_twelve_day_df.cnt.min()
    st.metric("Lowest Users Record", value=min_twelve_users)
with col4:
    mean_twelve_users = monthly_users_twelve_day_df.cnt.mean()
    st.metric("Average Users Record", value=mean_twelve_users)

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(30, 10))

sns.lineplot(x="dteday", y="cnt", data=monthly_users_twelve_day_df, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_title("Jumlah User per Month di 2012")
ax.tick_params(axis='y', labelsize=12)

st.pyplot(fig)



col1, col2, col3, col4 = st.columns(4)
 
with col1:
    st.metric("Highest Users Season: ", value="Fall")
with col2:
    fall_users = season_users_twelve_day_df.cnt.max()
    st.metric("Fall Users Record: ", value=fall_users)
with col3:
    st.metric("Highest Users Weather: ", value="Mist")
with col4:
    mist_users = weather_users_twelve_day_df.cnt.max()
    st.metric("Mist Users Record: ", value=mist_users)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(30, 10))

season_colors = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
weather_colors = ["#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="season", y="cnt", data=season_users_twelve_day_df, palette=season_colors, hue='season', ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Jumlah User per Musim di 2012")
ax[0].tick_params(axis='y', labelsize=12)

sns.barplot(x="weathersit", y="cnt", data=weather_users_twelve_day_df, palette=weather_colors, hue='weathersit', ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].set_title("Jumlah User Pada Tiap Cuaca di Tahun 2012", loc="center", fontsize=17)
ax[1].tick_params(axis ='y', labelsize=12)

st.pyplot(fig)
