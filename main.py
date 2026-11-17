import pandas as pd
import sqlite3 

data = "data/wait_times_data.xlsx"

df = pd.read_excel(data, sheet_name = "Table 1", header = 1, usecols = "A:H")
df_clean = df.dropna(subset=["Indicator result"])
df_clean = df_clean.drop(columns=["Region"])
df_clean = df_clean[df_clean["Province"] == "Ontario"]
print(df_clean.head(10))