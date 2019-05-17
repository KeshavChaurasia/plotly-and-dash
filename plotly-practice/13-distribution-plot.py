# distribution plot typically layer three plots on top of one another
# first layer = histogram where each data point is placed inside a bin of similar values
# second layer = rug-plot marks are placed along the xaxis for every data point which lets you see the distribution of values inside each bin
# third layer = distribution plat = kernel density estimat or KDE line that tries to describes the general shape of the distribution

import numpy as np
import plotly.offline as pyo
import plotly.figure_factory as ff

x1 = np.random.randn(200)-4
x2 = np.random.randn(200)-2
x3 = np.random.randn(200)+2
x4 = np.random.randn(200)+4


hist_data = [x1,x2,x3,x4]

group_label = ['X1','X2','X3','X4']

figure = ff.create_distplot(hist_data,group_label,bin_size=[1,2,3,4])

pyo.plot(figure,filename='13-distribution-plot.html')

