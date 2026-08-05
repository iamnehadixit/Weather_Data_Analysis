import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data/weather_data.csv') 
df["Date_Time"] = pd.to_datetime(df["Date_Time"])
df.to_csv("Data/weather_cleaned.csv",index = False)
# print(df)
#print(df.shape)
#print(df.columns)
#print(df.info()) 
#print(df.describe()) # Stastical summary
#print(df.isnull().sum())
#print(df.duplicated().sum())
#print(df.dtypes)
# print("\n========== WEATHER DATA ANALYSIS ==========")
# print("Temperature Analysis")
# print("Maximum Temparaturte:",df["Temperature_C"].max())
# print("Minimum Temparaturte:",df["Temperature_C"].min())
# print("Average Temparaturte:",df["Temperature_C"].mean())

# print("Humidity Analysis")
# print("Maximum Humidity:",df["Humidity_pct"].max())
# print("Minimum Humidity:",df["Humidity_pct"].min())
# print("Average Humidity:",df["Humidity_pct"].mean())

# print("Rainfall Analysis")
# print("Total Rainfall:",df["Precipitation_mm"].sum())
# print("Maximum Rainfall:",df["Precipitation_mm"].max())
# print("Average Rainfall:",df["Precipitation_mm"].mean())

# print("Wind Speed Analysis")
# print("Maximum Wind Speed:",df["Wind_Speed_kmh"].max())
# print("Minimum Wind Speed:",df["Wind_Speed_kmh"].min())
# print("Average Wind Speed:",df["Wind_Speed_kmh"].mean())

# print("Location Analysis")
# print("Locations:")
# for location in df["Location"].unique():
#     print(location)
# print(df["Location"].value_counts())

# print("Average Temperature by location:",df.groupby("Location")["Temperature_C"].mean().sort_values(ascending=False))
# print("Average Humidity by location:",df.groupby("Location")["Humidity_pct"].mean().sort_values(ascending=False))
# print("Average Wind Speed by location:",df.groupby("Location")["Wind_Speed_kmh"].mean().sort_values(ascending=False))
# print("Total Rainfall by location:",df.groupby("Location")["Precipitation_mm"].sum().sort_values(ascending=False))

# plt.figure(figsize=(8,5))
# plt.hist(df["Temperature_C"],bins=40,color="#eda726",edgecolor="black")
# plt.title("Temperature Distribution")
# plt.xlabel("Temperature (°C)")
# plt.ylabel("Frequency")
# plt.grid(color="#bfbeba")
# plt.show()
# plt.tight_layout()
# plt.savefig("Images/temperature_distribution.png")


# avg_temp = df.groupby("Location")["Temperature_C"].mean()
# plt.figure(figsize=(10,5))
# plt.bar(avg_temp.index, avg_temp.values, color="#e3950e")
# plt.title("Average Temperature by Location")
# plt.xlabel("Location")
# plt.ylabel("Temperature (°C)")
# plt.xticks(rotation=45)
# plt.grid(color="#bfbeba")
# plt.show()
# plt.tight_layout()
# plt.savefig("Images/avg_temperature_location.png")


# avg_humd = df.groupby("Location")["Humidity_pct"].mean()
# plt.figure(figsize=(10,5))
# plt.bar(avg_humd.index, avg_humd.values,color="#e685ad")
# plt.title("Average Humdity by Location")
# plt.xlabel("Location")
# plt.ylabel("Humidity")
# plt.xticks(rotation=45)
# plt.grid(color="#bfbeba")
# plt.show()
# plt.tight_layout()
# plt.savefig("Images/avg_humidity_location.png")

# wnd_speed = df.groupby("Location")["Wind_Speed_kmh"].mean()
# plt.figure(figsize=(10,5))
# plt.bar(wnd_speed.index, wnd_speed.values,color="#7af090")
# plt.title("Average Wind Speed by Location")
# plt.xlabel("Location")
# plt.ylabel("Wind speed")
# plt.xticks(rotation=45)
# plt.grid(color="#bfbeba")
# plt.show()
# plt.tight_layout()
# plt.savefig("Images/avg_windspeed_location.png")

# rainfall = df.groupby("Location")["Precipitation_mm"].mean()
# plt.figure(figsize=(10,5))
# plt.bar(rainfall.index, rainfall.values,color="#67c5eb")
# plt.title("Average Rainfall by Location")
# plt.xlabel("Location")
# plt.ylabel("Rainfall")
# plt.xticks(rotation=45)
# plt.grid(color="#bfbeba")
# plt.show()
# plt.tight_layout()
# plt.savefig("Images/avg_rainfall_location.png")

# plt.figure(figsize=(12,5))
# plt.plot(df["Temperature_C"][:100], color="orange", label="Temperature")
# plt.plot(df["Humidity_pct"][:100], color="pink", label="Humidity")
# plt.legend()
# plt.title("Temperature vs Humidity")
# plt.xlabel("Temperature (°C)")
# plt.ylabel("Humidity (%)")
# plt.grid(color="#bfbeba")
# plt.show()
# plt.tight_layout()
# plt.savefig("Images/temp_vs_humidity.png")

top_temp = df.groupby("Location")["Temperature_C"].mean().sort_values(ascending=False)

print("Top 5 Hottest Locations")
print(top_temp.head())
print("Top 5 Coldest Locations")
print(top_temp.tail())

summary = df.groupby("Location").agg({
    "Temperature_C": "mean",
    "Humidity_pct": "mean",
    "Wind_Speed_kmh": "mean",
    "Precipitation_mm": "mean"
})
print(summary)
summary.to_csv("Data/weather_summary.csv", index=True)

print("\n===== WEATHER DATASET SUMMARY =====")
print("Total Records:", len(df))
print("Locations:", df["Location"].nunique())
print("Highest Temperature:", df["Temperature_C"].max())
print("Lowest Temperature:", df["Temperature_C"].min())
print("Average Humidity:", df["Humidity_pct"].mean())
print("Highest Wind Speed:", df["Wind_Speed_kmh"].max())

print("\n========== KEY INSIGHTS ==========")

print(f"• {summary['Temperature_C'].idxmax()} has the highest average temperature.")
print(f"• {summary['Humidity_pct'].idxmax()} has the highest average humidity.")
print(f"• {summary['Wind_Speed_kmh'].idxmax()} has the highest average wind speed.")
print(f"• {summary['Precipitation_mm'].idxmax()} has the highest average rainfall.")
print(f"• Weather data is analyzed for {len(summary)} locations.")