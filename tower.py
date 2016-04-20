#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import integrate

t, v = np.loadtxt('droptower_vdata.txt', unpack=True)
x = integrate.cumtrapz(v, t, initial=0)
diffs = list(np.diff(v))

dt = t[1] - t[0]
a = []
a.append(diffs[0]/dt)
for dv in diffs:
	a.append(dv/dt)

# Todo: Uncomment the type of plotting you want

'''
# One figure with three subplots
f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
ax1.plot(t,x,color='r')
ax1.set_title('Position')
ax1.set_xlim([0,10])
ax1.set_ylim([-35, 35])
ax2.plot(t,v,color='b')
ax2.set_title('Velocity')
ax3.plot(t,a,color='c')
ax3.set_title('Acceleration')
'''

'''
# Three individual figures for each plot
plt.figure(1)
plt.plot(t, x)
plt.title('Droptower Position')
plt.xlabel('Time')
plt.ylabel('Position')

plt.figure(2)
plt.plot(t, v)
plt.title('Droptower Velocity')
plt.xlabel('Time')
plt.ylabel('Velocity')

plt.figure(3)
plt.plot(t, a)
plt.title('Droptower Acceleration')
plt.xlabel('Time')
plt.ylabel('Acceleration')
'''

'''
# All plots on same figure
z = (x, v, a)
labels = ('position', 'velocity', 'acceleration')

for y, name in zip(z, labels):
	plt.plot(t,y, label=name)

x_axis = np.zeros(len(x))
plt.plot(t, x_axis, '--')
plt.legend()
plt.title('Droptower Kinematics')
'''

a = [elem for elem in a if elem > 0] # Filter out acceleration values < 0
sum_a = np.sum(a)
avg_a = sum_a/len(a)
print('Average upward acceleration = %f m/s/s\n') %avg_a

plt.show()