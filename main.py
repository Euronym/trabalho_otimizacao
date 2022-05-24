# Script based in the paper "Providing Wireless Coverage to High-rise Buildings Using UAVs"
#  
# Author : Bruno Santos Martins

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
import math

G = 10E9

building_height = [0, 200]

building_width = [0, 50]

xx, yy = np.meshgrid(np.arange(50), np.arange(50))

carrier_frequency = 2 * G

g1, g2, g3, g4 = 32.4, 14, 15, 0.5 

w = 20

step_size = 0.01

n_users_floor = 20

height_floors = 5

max_iterations = 500
# total number of floors 
#n_floors = round(building_dimensions[2] / height_floors)
# coordinates of users in the building
#coordinates_users = np.ones((n_floors, 20, 3)) 
# angle between uav and users 
#theta_users = np.ones((n_floors, 20))
# initial coordinates of the uav
coordinates_uav = [0, 0, 0]

distance_user_building, distance_drone_user, theta = 0, 0, 0  

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.plot3D(50, 50, 0)

#m_1 = 

#m_2 = 

'''
l_1, l_2, l_3 = 0, 0, 0

for i in range(n_users_floor * n_floors):

    k = w * np.log10(carrier_frequency) + g1 + g2 + g4 * distance_2d_user_drone

    l_1 += w * np.log10(distance_drone_user) + g3 * (1 - math.cos(theta_users[i])) ** 2

    l_2 += w * np.log10(distance_drone_user) + g3 * (1 - math.cos(theta_users[i])) ** 2 + k 

L_total = l_1 + l_2 + l_3
'''