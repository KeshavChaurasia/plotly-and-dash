# A histogram displays an accurate representation of the overall distributionn of a continuous feature
# to create a histogram, we divide the entire range of values of the continuous feature into a series of intervals
# this series of intervals are known as bins

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mpg.csv')
data =[go.Histogram(x=df['mpg'],xbins=dict(start=0,end=50,size=1))]

layout=go.Layout(title='Histogram')

figure = go.Figure(data=data,layout=layout)

pyo.plot(figure,filename='11-histogram.html')