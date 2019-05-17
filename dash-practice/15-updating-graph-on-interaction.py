import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input,Output
import numpy as np
import pandas as pd
from numpy import random

app = dash.Dash()
df = pd.read_csv('data/mpg.csv')

# adding noise or jitter

df['year'] = random.randint(-4,5,len(df))*0.1 + df['model_year']

ScatterGraph = dcc.Graph(
	id='mpg-scatter',
	figure = dict(
		data = [go.Scatter(
			x=df['year']+1900,
			y=df['mpg'],
			text=df['name'],
			hoverinfo='text',mode='markers')],
		layout = go.Layout(
			title='MPG Data',
			xaxis=dict(
				title='Model Year'),
			yaxis=dict(
				title='MPG'),
			hovermode='closest')
		)
	)

MpgLineScatter = dcc.Graph(
	id='mpg-line',
	figure = dict(
		data = [go.Scatter(
			x=[0,1],
			y=[0,1],
			mode='lines'
		)],
		layout = go.Layout(
			title='Acceleration',
			margin={'l':0}
		)
	)
)

Markdown = dcc.Markdown(
	id='mpg-status',
)

app.layout = html.Div([
	html.Div([
		ScatterGraph
	],style={'width':'50%','display':'inline-block'}),
	html.Div([
		MpgLineScatter
	],style={'width':'50%','display':'inline-block'}),
	html.Div([
		Markdown
	])
])


@app.callback(Output('mpg-line','figure'),
	[Input('mpg-scatter','hoverData')])
def callback_graph(hoverData):
	v_index = hoverData['points'][0]['pointIndex']
	figure = dict(
		data=[go.Scatter(
			x=[0,1],
			y=[0,60/df.iloc[v_index]['acceleration']],
			mode='lines',
			line = {'width':2*df.iloc[v_index]['cylinders']}
		)],
		layout=go.Layout(
			title=df.iloc[v_index]['name'],
			xaxis = dict(visible=False),
			yaxis = dict(visible=False,range=[0,60/df['acceleration'].min()]),
			hovermode='closest',
			margin={'l':0},
			height=300
		)
	)
	return figure

@app.callback(Output('mpg-status','children'),
	[Input('mpg-scatter','hoverData')])
def callback_stats(hoverData):
	v_index = hoverData['points'][0]['pointIndex']
	stats = '''
			{} cylinders
			{} cc displacement
			0-60mph in {} seconds
			'''.format(df.iloc[v_index]['cylinders'],df.iloc[v_index]['displacement'],df.iloc[v_index]['acceleration'])
	return stats

if __name__ == '__main__':
	app.run_server()