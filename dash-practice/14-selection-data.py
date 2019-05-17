import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input,Output
import numpy as np
import pandas as pd
import json
import base64




app = dash.Dash()

np.random.seed(10)


# Create Data
x1 = np.linspace(0.1,5,50)
x2 = np.linspace(5.1,10,50)
y = np.random.randint(0,50,50)

# Create Dataframe
df1 = pd.DataFrame({'x':x1,'y':y})
df2 = pd.DataFrame({'x':x1,'y':y})
df3 = pd.DataFrame({'x':x2,'y':y})


df = pd.concat([df1,df2,df3])

ScatterGraph = dcc.Graph(
	id='plot',
	figure = dict(
		data=[go.Scatter(
			x=df['x'],
			y=df['y'],
			mode='markers',
			marker={'size':8})],
		layout=go.Layout(
			title='Density',
			xaxis=dict(title='x'),
			yaxis=dict(title='y'),
			hovermode='closest')
	)
)


app.layout=html.Div([
	html.Div(ScatterGraph),
	html.Div(html.Pre(id='density',style={'paddingTop':25}))
])




@app.callback(Output('density','children'),
	[Input('plot','selectedData')])
def find_density(selectedData):
	pts = len(selectedData['points'])
	rng_or_lp = list(selectedData.keys())
	rng_or_lp.remove('points')
	max_x = max(selectedData[rng_or_lp[0]]['x'])
	min_x = min(selectedData[rng_or_lp[0]]['x'])
	max_y = max(selectedData[rng_or_lp[0]]['y'])
	min_y = min(selectedData[rng_or_lp[0]]['y'])
	area = (max_x-min_x) * (max_y-min_y)
	d = pts/area
	return "Density: {:.2f}".format(d)



if __name__ == '__main__':
	app.run_server()