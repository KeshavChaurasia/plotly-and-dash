import dash
import dash_html_components as html
import dash_core_components as dcc


app = dash.Dash()



markdown_text = '''
# this is MarkDown
## Dash and markdown

this is a test example. here you can use markdown in the plotly.
Isn't it cool??
:-)

'''


app.layout = html.Div([
	html.Label('MarkDown'),
	dcc.Markdown(children=markdown_text),
	html.Label('Dropdown'),
	dcc.Dropdown(
		options=[
			{'label':'New York City','value':'NYC'},
			{'label':'San Franscisco','value':'SF'}],
		value='SF'),
	html.Label('Slider'),
	dcc.Slider(
		min=1,
		max=10,
		step=0.5,
		value=0,
		marks={i: i for i in range(1,10)}),
	html.Label('Some Radio Items'),
	dcc.RadioItems(
		options=[
			{'label':'New York City','value':'NYC'},
			{'label':'San Franscisco','value':'SF'}],
		value='SF')
	])


print(f"dcc version {dcc.__version__}")



if __name__ == '__main__':
	app.run_server()