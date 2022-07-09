import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


#df = pd.read_csv('2022.csv')
df = pd.read_csv('2020-2022.csv')
len(df)
df = df.loc[ (df['Transaction Type'] == 'Sales') & (df['Registration type'] == 'Off-Plan')]
len(df)
df = df.loc[ (df['Property Type'] == 'Unit')     & (df['Property Sub Type'] == 'Flat')]
len(df)
df = df.loc[ (df['Property Size (sq.m)'] > 20)]
len(df)

df = df[['Transaction Date', 'Area', 'Amount', 'Property Size (sq.m)', 'Room(s)']]

df.index = pd.to_datetime(df['Transaction Date'])

df = df.assign(size_f  = df['Property Size (sq.m)']*10.7639)
df = df.assign(price_f = (df['Amount']/df['size_f']).round())

df = df.astype({'price_f':'int'})

df.groupby(pd.Grouper(freq='M')).size()

df.groupby(['Area']).size().sort_values(ascending=False).head(10)
