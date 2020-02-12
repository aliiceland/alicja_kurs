import pandas as pd 

df=pd.read_csv("../logi.csv", delimiter=";", header=None)

print(df.head())

df.to_excel("logi.xlsx", header=False, index=False)


