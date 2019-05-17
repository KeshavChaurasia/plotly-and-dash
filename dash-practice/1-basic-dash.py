# Created dashboard in python
# dash is declrative

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {
'background':'#111111',
'text':'#7FDBFF'}

app.layout = html.Div(children=[
	html.H1('Hello Dash!',style={'textAlign':'center','color':colors['text']}),
	dcc.Graph(id='example',
		figure=dict(
			data=[
				{'x':[1,2,3,4,5],'y':[4,1,2,3,4],'type':'bar','name':'SF'},
				{'x':[1,2,3,4],'y':[10,11,12,5,3],'type':'bar','name':'NYC'}],
			layout=dict(
				plot_bgcolor=colors['background'],
				title='BAR PLOTS',
				paper_bgcolor=colors['background'],
				font=dict(color=colors['text'])
			)))],style={'background':colors['background']})

if __name__ == '__main__':
	app.run_server()
