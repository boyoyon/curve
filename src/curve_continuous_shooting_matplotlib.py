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

plt.plot(t, x, y, lw=LWIDTH, color='orange')
plt.plot(t, x, [config.proj_y] * config.nr_points, lw=LWIDTH, color='blue')
plt.plot(t, [config.proj_x] * config.nr_points, y, lw=LWIDTH, color='green')
plt.plot([config.proj_t] * config.nr_points, x, y, lw=LWIDTH, color='darkgray')

plt.tight_layout()

elevation = config.elevation

for i, azimuth in enumerate(np.arange(config.azimuth_start, config.azimuth_end, config.azimuth_step)):

    ax.view_init(elev=elevation, azim=azimuth)

    dst_path = '%04d.png' % (i+1)
    plt.savefig(dst_path)
    print('save %s' % dst_path)

