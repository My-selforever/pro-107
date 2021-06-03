import pandas as pd
import plotly_express as px
import os

os.system('cls')

student = input('Student ID: ')

f = open('data.csv')

df = pd.read_csv('data.csv')

location = df.loc[df['student_id'] == student]

print(location)

graph = px.bar(location, x=['Level 1', 'Level 2', 'Level 3',
               'Level 4'], y=location.groupby('level')['attempt'].mean())

graph.show()