# heatmas allow the visualization of three features
# X and Y represent grids for categorical feature
# Z represents continuous values for those X and Y -- color scale


import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from plotly import tools


df1 = pd.read_csv('data/2010SantaBarbaraCA.csv')
df2 = pd.read_csv('data/2010SitkaAK.csv')
df3 = pd.read_csv('data/2010YumaAZ.csv')

trace1 = go.Heatmap(
	x=df1['DAY'],
	y=df1['LST_TIME'],
	z=df1['T_HR_AVG'].values.tolist(),
	colorscale='Jet',
	zmin=5,
	zmax=40)

trace2 = go.Heatmap(
	x=df2['DAY'],
	y=df2['LST_TIME'],
	z=df2['T_HR_AVG'].values.tolist(),
	colorscale='Jet',
	zmin=5,
	zmax=40)

trace3 = go.Heatmap(
	x=df3['DAY'],
	y=df3['LST_TIME'],
	z=df3['T_HR_AVG'].values.tolist(),
	colorscale='Jet',
	zmin=5,
	zmax=40)

figure = tools.make_subplots(
	rows=1,
	cols=3,
	subplot_titles=['2010SantaBarbaraCA','2010SitkaAK','2010YumaAZ'],
	shared_yaxes=True)


figure.append_trace(trace1,1,1)
figure.append_trace(trace2,1,2)
figure.append_trace(trace3,1,3)

figure['layout'].update(title='Temps for 3 cities')


pyo.plot(figure,filename='15-heatmap.html')


