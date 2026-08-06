import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/weather_cleaned.csv")
plt.figure(figsize=(18, 12))
plt.suptitle("Weather Data Analysis Dashboard")

avg_temp = df.groupby("Location")["Temperature_C"].mean()
plt.subplot(2,2,1)
plt.bar(avg_temp.index, avg_temp.values,color="#e3950e")
plt.title("Average Temperature")
plt.xticks(rotation=45)

avg_humidity = df.groupby("Location")["Humidity_pct"].mean()
plt.subplot(2,2,2)
plt.bar(avg_humidity.index,avg_humidity.values,color="#e685ad")
plt.title("Average Humidity")
plt.xticks(rotation=45)

avg_wind = df.groupby("Location")["Wind_Speed_kmh"].mean()
plt.subplot(2,2,3)
plt.bar(avg_wind.index,avg_wind.values,color="#7af090")
plt.title("Average Wind Speed")
plt.xticks(rotation=45)

avg_rain = df.groupby("Location")["Precipitation_mm"].mean()
plt.subplot(2,2,4)
plt.bar(avg_rain.index,avg_rain.values,color="#67c5eb")
plt.title("Average Rainfall")
plt.xticks(rotation=45)

plt.tight_layout(rect=[0,0,1,0.96])

plt.savefig("Images/weather_dashboard.png")
plt.show()