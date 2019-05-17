import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# creating a dataset
df = pd.read_csv('data/2010YumaAZ.csv')
days = df['DAY'].unique()

data = [go.Scatter(x=df['LST_TIME'],y=df[df['DAY']==day]['T_HR_AVG'],mode='lines',name=day) for day in days]

layout = go.Layout(title='Daily Temperature average')

figure = go.Figure(data=data,layout=layout)

pyo.plot(figure,filename='4-line-charts-exercise.html')
