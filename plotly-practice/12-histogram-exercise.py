import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/abalone.csv')

data = [go.Histogram(x=df['length'],xbins=dict(start=0,end=1,size=0.02))]

layout=go.Layout(title='Histogram')

figure = go.Figure(data=data,layout=layout)

pyo.plot(figure,filename='12-histogram-exercise.html')
