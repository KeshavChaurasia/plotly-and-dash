import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/abalone.csv',index_col=0)

data = [go.Bar(x=df.index,y=df[response],name=response) for response in df.columns]

# for horizontal
# reverse x and y and add orientation = 'h' in the trace

#data = [go.Bar(x=df[response],y=df.index,name=response,orientation='h') for response in df.columns]


layout = go.Layout(title='Survey Results',barmode='stack')

figure = go.Figure(data=data,layout=layout)

pyo.plot(figure,filename='6-bar-chart-exercise.html')


