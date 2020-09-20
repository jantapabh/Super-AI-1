# Pandas 

import pandas as pd

df = pd.read_csv('digidb.csv')
print(df)
type(df)
df.head(3)
df.sample(5)
df.columns

for col in df.columns:
  col_mode = df[col].mode()[0]
  # print(col, col_mode)
  df[col] = df[col].fillna(col_mode)
 df.isna().sum()

#Show descriptive or summary statistics
 df.describe()

 