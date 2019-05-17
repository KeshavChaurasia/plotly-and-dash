import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mpg.csv')
app = dash.Dash()

features = df.columns

app.layout = html.Div([
	html.Div([
		dcc.Dropdown(id='xaxis',options=[{'label':feature,'value':feature} for feature in features],value='displacement')
	],style={'width':'48%','display':'inline-block'}),
	html.Div([
		dcc.Dropdown(id='yaxis',options=[{'label':feature,'value':feature} for feature in features],value='mpg')
	],style={'width':'48%','display':'inline-block'}),
	dcc.Graph(id='feature-graphic')
],style={'padding':10})



@app.callback(Output('feature-graphic','figure'),
	[
		Input('xaxis','value'),
		Input('yaxis','value')])
def update_graph(xaxis_name,yaxis_name):
	data = [go.Scatter(x=df[xaxis_name],y=df[yaxis_name],mode='markers',text=df['name'],marker={'opacity':0.5})]
	layout = go.Layout(title='Scatter Plot with two input',xaxis=dict(title=xaxis_name),yaxis=dict(title=yaxis_name),hovermode='closest')
	return {'data':data,'layout':layout}

if __name__ == '__main__':
	app.run_server()