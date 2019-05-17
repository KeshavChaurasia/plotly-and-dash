import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input,Output
import pandas as pd
import json
import base64




app = dash.Dash()

df = pd.read_csv('data/wheels.csv')


def encode_image(image_file):
	encoded = base64.b64encode(open(image_file,'rb').read())
	return 'data:image/png;base64,{}'.format(encoded.decode())

ScatterGraph = dcc.Graph(
	id='wheels-plot',
	figure = dict(
		data=[go.Scatter(
			x=df['color'],
			y=df['wheels'],
			dy=1,
			mode='markers',
			marker={'size':12})],
		layout=go.Layout(
			title='Hover Data Visualization',
			xaxis=dict(title='Color'),
			yaxis=dict(title='Wheels'),
			hovermode='closest')
	)
)


app.layout=html.Div([
	html.Div(ScatterGraph),
	html.Div(html.Img(id='hover-data',src='children',height=300))
])



@app.callback(Output('hover-data','src'),
	[Input('wheels-plot','clickData')])
def callback_image(hoverData):
	wheel = hoverData['points'][0]['y']
	color = hoverData['points'][0]['x']
	path = 'data/Images/'
	file = df[(df['wheels']==wheel)& (df['color']==color)]['image'].values[0]
	return encode_image(path+file)
	return json.dumps(hoverData,indent=2)


if __name__ == '__main__':
	app.run_server()