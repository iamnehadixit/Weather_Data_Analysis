import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data/weather_data.csv') 
df["Date_Time"] = pd.to_datetime(df["Date_Time"])
df.to_csv("Data/weather_cleaned.csv",index = False)
print(df)
#print(df.shape)
#print(df.columns)
#print(df.info()) 
#print(df.describe()) # Stastical summary
#print(df.isnull().sum())
#print(df.duplicated().sum())
#print(df.dtypes)
print("\n===== WEATHER DATASET SUMMARY =====")
print("Temperature Analysis")
print("Maximum Temparaturte:",df["Temperature_C"].max())
print("Minimum Temparaturte:",df["Temperature_C"].min())
print("Average Temparaturte:",df["Temperature_C"].mean())

print("Humidity Analysis")
print("Maximum Humidity:",df["Humidity_pct"].max())
print("Minimum Humidity:",df["Humidity_pct"].min())
print("Average Humidity:",df["Humidity_pct"].mean())

print("Rainfall Analysis")
print("Total Rainfall:",df["Precipitation_mm"].sum())
print("Maximum Rainfall:",df["Precipitation_mm"].max())
print("Average Rainfall:",df["Precipitation_mm"].mean())

print("Wind Speed Analysis")
print("Maximum Wind Speed:",df["Wind_Speed_kmh"].max())
print("Minimum Wind Speed:",df["Wind_Speed_kmh"].min())
print("Average Wind Speed:",df["Wind_Speed_kmh"].mean())

print("Location Analysis")
print("Locations:")
for location in df["Location"].unique():
    print(location)
print(df["Location"].value_counts())

print("Average Temperature by location:",df.groupby("Location")["Temperature_C"].mean().sort_values(ascending=False))
print("Average Humidity by location:",df.groupby("Location")["Humidity_pct"].mean().sort_values(ascending=False))
print("Average Wind Speed by location:",df.groupby("Location")["Wind_Speed_kmh"].mean().sort_values(ascending=False))
print("Total Rainfall by location:",df.groupby("Location")["Precipitation_mm"].sum().sort_values(ascending=False))