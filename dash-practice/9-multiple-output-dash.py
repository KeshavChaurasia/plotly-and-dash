import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import pandas as pd
import base64

df = pd.read_csv('data/wheels.csv')

app = dash.Dash()


def encode_image(image_file):
	encoded = base64.b64encode(open(image_file,'rb').read())
	return 'data:image/png;base64,{}'.format(encoded.decode())



app.layout = html.Div([
	dcc.RadioItems(
					id='wheels',
					options=[{'label':i,'value':i} for i in df['wheels'].unique()],
					value=1
					),
	html.Div(id='wheels-output'),
	html.Hr(),
	dcc.RadioItems(
					id='colors',
					options=[{'label':i,'value':i} for i in df['color'].unique()],
					value='blue'
					),
	html.Div(id='colors-output'),
	html.Img(id='display-image',src='children',height=300)
],style={'fontFamily':'helvetica',})


@app.callback(
	Output('wheels-output','children'),
	[Input('wheels','value')])
def callback_a(wheels_value):
	return "you chose {}".format(wheels_value)


@app.callback(
	Output('colors-output','children'),
	[Input('colors','value')])
def callback_b(colors_value):
	return "you chose {}".format(colors_value)


@app.callback(Output('display-image','src'),
	[Input('wheels','value'),Input('colors','value')])
def callback_image(wheels_value,colors_value):
	path = 'data/Images/'
	image = df[(df['wheels']==wheels_value) & (df['color']==colors_value)]['image'].values[0]
	print(image)
	return encode_image(path+image)

if __name__ == '__main__':
	app.run_server()