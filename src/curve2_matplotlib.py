import os
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from config import *

ini_file = os.path.join(os.path.dirname(__file__), 'config.ini')
config = CONFIG(ini_file)

LWIDTH = 5

#Create data
t = np.linspace(config.tmin, config.tmax, config.nr_points)
x = eval(config.xt)
y = eval(config.yt)

ax = plt.axes(projection='3d')

for ti, xi, yi in zip(t, x, y):
    plt.plot([ti, ti],[0,xi], [0, yi], color='orange')

for ti, xi in zip(t, x):
    #plt.plot([ti, ti], [0, xi],config.proj_y, color='green')
    plt.plot([ti, ti], [0, xi],[config.proj_y,config.proj_y], color='green')

for ti, yi in zip(t, y):
    plt.plot([ti, ti],[config.proj_x, config.proj_x], [0, yi], color='blue')

plt.tight_layout()

plt.show()

