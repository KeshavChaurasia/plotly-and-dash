import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv('data/iris.csv')


trace0=df[df['class']=='Iris-setosa']['petal_length']
trace1=df[df['class']=='Iris-versicolor']['petal_length']
trace2=df[df['class']=='Iris-virginica']['petal_length']


hist_data=[trace0,trace1,trace2]

group_labels= ['Iris-Setosa','iris-versicolor','iris-virginica']

figure = ff.create_distplot(hist_data,group_labels)

pyo.plot(figure,filename='14-distribution-plot-exercise.html')
