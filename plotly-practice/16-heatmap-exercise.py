import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/flights.csv')


data = [go.Heatmap(x=df['year'],y=df['month'],z=df['passengers'])]

layout=go.Layout(title='Heatmap for passengers')

figure = go.Figure(data=data,layout=layout)

pyo.plot(figure,filename='16-heatmap-exercise.html')
