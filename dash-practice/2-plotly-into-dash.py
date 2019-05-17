# use plotly into dash to make dashboard
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

# creating web app
app = dash.Dash()

# creating data
np.random.seed(42)

random_x = np.random.randint(-101,101,100)
random_y = np.random.randint(-101,101,100)

data = [go.Scatter(
	x=random_x,
	y=random_y,
	mode='markers',
	marker=dict(
		size=4,
		color='rgb(51,204,153)',
		symbol='circle',
		line=dict(width=2)
	))]
layout  = go.Layout(
	title="Scatter Plot",
	xaxis={'title':'X-axis'},
	yaxis=dict(title='Y-axis'),
	hovermode='closest')

app.layout = html.Div([
	dcc.Graph(
		id='scatterplot',
		figure = dict(data=data,layout=layout)),
	dcc.Graph(
		id='scatterplot2',
		figure = dict(data=data,layout=layout))

	])



if __name__ == '__main__':
	app.run_server()