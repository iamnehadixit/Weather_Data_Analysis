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