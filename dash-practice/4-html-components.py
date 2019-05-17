import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(
	['This is the outermost div!',
	html.Div(
		['this is an inner div'],
		style={'color':'red','border':'1px red solid'})],
	style={'color':'green','border':'2px green solid'}
	)

if __name__=="__main__":
	app.run_server()