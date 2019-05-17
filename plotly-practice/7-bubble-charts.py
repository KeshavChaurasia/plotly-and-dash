# similar to the scatter plot but has an extra dimension like size
# multiple feature can be graphed

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/mpg.csv')

data = [go.Scatter(
	x=df['horsepower'],
	y=df['mpg'],
	text=df['name'],
	mode='markers',
	marker=dict(
		size=df['weight']/1000,
		color=df['cylinders'],
		showscale=True))]

layout= go.Layout(title='Bubble Chart')
figure = go.Figure(data=data,layout=layout)
pyo.plot(figure,filename='7-bubble-charts.html')
