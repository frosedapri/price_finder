import pandas as pd


data = pd.read_csv("data.ods", sep=";")

print(data.head())