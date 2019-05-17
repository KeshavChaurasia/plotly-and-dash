# box plot visualizes the variation of a feature by depicting the continuous numerical data through quartiles
# we can then separate the data based on a categoical feature to compare the continuous feature based on category

import plotly.offline as pyo
import plotly.graph_objs as go

snodgrass = [50,100,110,111,132,123,120,120,113,115,112,135,250]
twain = [5,45,50,50,55,60,63,58,65,52,52,65,70,150]

data = [go.Box(y=snodgrass,name='snodgrass'),go.Box(y=twain,name='twain')]

pyo.plot(data,filename='9-box-plots.html')

