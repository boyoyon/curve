from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#Define function
def odef(xyz,t,sigma,rho,beta):
    x,y,z = xyz
    return [sigma*(y-x),x*(rho-z)-y,x*y -beta*z]

#Create data
t = np.linspace(0,25,10000)
xyz0 = [1,1,1]
sigma, rho, beta = 8, 28, 8/3

#Integrate under function
xyz = odeint(odef,xyz0,t, args=(sigma,rho,beta))

#Create figure

ax = plt.axes(projection='3d')
ax.set_aspect('equal')
ax.plot(xyz[:,0],xyz[:,1],xyz[:,2],alpha=0.5)
plt.tight_layout()
plt.show()
