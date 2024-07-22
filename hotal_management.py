# HOTEL BOOKING
# import libraries
import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns 
import warnings
warnings.filterwarnings("ignore")

# LOADING DATA SETS
df=pd.read_csv("C:\\Users\\hp\\Desktop\\hotel_bookings 2.csv")

# EXPLORING DATA ANALYSIS AND DATA CLEANING
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'],dayfirst=True)
print(df.info()) 
print(df.describe(include="object"))
for col in df.describe(include="object").columns:
    print(col)
    print(df[col].unique())
    print("_ _"*50)
print(df.isnull().sum())
df.drop(["company","agent"],inplace=True,axis=1)
df.dropna(inplace=True)
print(df.isnull().sum())
print(df.describe())
df["adr"].plot(kind="box")
plt.show()
df=df[df["adr"]<5000]
print(df.describe())

#   DATA ANALYSIS AND VISUALIZATIONS
cancelled_perc=df["is_canceled"].value_counts(normalize=True)
print(cancelled_perc)

plt.figure(figsize=(5,5))
plt.title("reservation status")
plt.bar(["not canceled","canceled"],df["is_canceled"].value_counts(),edgecolor="k",width=0.7)
plt.show()

plt.figure(figsize=(8,6))
ax1=sns.countplot(x="hotel",hue="is_canceled",data=df,palette="Greens")
legend_labels,_=ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title("reservation status in diff hotels",size=20)
plt.xlabel("hotel")
plt.ylabel("number of reservations")
plt.show()

resort_hotel=df[df["hotel"]=="Resort Hotel"]
print(resort_hotel["is_canceled"].value_counts(normalize=True))

city_hotel=df[df["hotel"]=="City Hotel"]
print(city_hotel["is_canceled"].value_counts(normalize=True))

# check price effect on hotel cancel
resort_hotel=resort_hotel.groupby("reservation_status_date")[["adr"]].mean()
city_hotel=city_hotel.groupby("reservation_status_date")[["adr"]].mean()

# visualization
plt.figure(figsize=(20,8))
plt.title("average daily rate in city and resort hotel",fontsize=50)
plt.plot(resort_hotel.index,resort_hotel["adr"],label="Resort Hotel")
plt.plot(city_hotel.index,city_hotel["adr"],label="city Hotel")
plt.show()

df["month"]=df["reservation_status_date"]
plt.figure(figsize=(10,8))
ax1=sns.countplot(x="month",hue="is_canceled",data=df,palette="bright")
legend_labels,_=ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title("reservation status per month",size=20)
plt.xlabel("month")
plt.ylabel("number of reservations")
plt.legend("not canceled","canceled")
plt.show()



# top 10 country
cancelled_data=df[df["is_canceled"]==1]
top_10_country=cancelled_data["country"].value_counts()[:10]
plt.figure(figsize=[8,8])
plt.title("top 10 countries with reservation canceled")
plt.pie(top_10_country,autopct="%.2f",labels=top_10_country.index)
plt.show()

# how the booking is done either direct or online
print(df["market_segment"].value_counts())
print(df["market_segment"].value_counts(normalize=True))
print(cancelled_data["market_segment"].value_counts(normalize=True))

cancelled_df_adr=cancelled_data.groupby("reservation_status_date")[["adr"]].mean()
cancelled_df_adr.reset_index(inplace=True)
cancelled_df_adr.sort_values("reservation_status_date")[["adr"]].mean()

not_cancelled_data=df[df["is_canceled"]==0]
not_cancelled_df_adr=not_cancelled_data.groupby("reservation_status_date")[["adr"]].mean()
not_cancelled_df_adr.reset_index(inplace=True)
not_cancelled_df_adr.sort_values("reservation_status_date")[["adr"]].mean()
plt.figure(figsize=(20,6))
plt.title("average daily rate")
plt.plot(not_cancelled_df_adr["reservation_status_date"],not_cancelled_df_adr["adr"],label="not cancelled")
plt.plot(cancelled_df_adr["reservation_status_date"],cancelled_df_adr["adr"],label="cancelled")
plt.legend()
plt.show()

# 
cancelled_df_adr=cancelled_df_adr[(cancelled_df_adr["reservation_status_date"]>"2016") & (cancelled_df_adr["reservation_status_date"]<"2017-09")]
not_cancelled_df_adr=not_cancelled_df_adr[(not_cancelled_df_adr["reservation_status_date"]>"2016")  & (not_cancelled_df_adr["reservation_status_date"]<"2017-09")]

plt.figure(figsize=(20,6))
plt.title("average daily rate",fontsize=30)
plt.plot(not_cancelled_df_adr["reservation_status_date"],not_cancelled_df_adr["adr"],label="not cancelled")
plt.plot(cancelled_df_adr["reservation_status_date"],cancelled_df_adr["adr"],label="cancelled")
plt.legend(fontsize=20)
plt.show()