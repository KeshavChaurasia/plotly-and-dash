import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv('data/abalone.csv')

a = np.random.choice(df['rings'],30,replace=False)
b = np.random.choice(df['rings'],20,replace=False)

data = [go.Box(y=a,name='A'),go.Box(y=b,name='B')]

layout = go.Layout(title='2 Random Sample')

figure = go.Figure(data=data,layout=layout)

pyo.plot(figure,filename='10-box-plot-exercise.html')

