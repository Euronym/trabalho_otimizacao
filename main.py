# Script based in the paper "Providing Wireless Coverage to High-rise Buildings Using UAVs"
#  
# Author : Bruno Santos Martins

import numpy as np
import math

G = 10E9

building_dimensions = (200, 250, 300) 

carrier_frequency = 2 * G

g1, g2, g3, g4 = 32.4, 14, 15, 0.5 

w = 20

step_size = 0.01

n_users_floor = 20

height_floors = 5

max_iterations = 500

n_floors = round(building_dimensions[2] / height_floors)

coordinates_users = np.ones((n_floors, 20, 3)) 

theta_users = np.ones((n_floors, 20))

coordinates_uav = [0, 0, 0]

distance_user_building, distance_drone_user, theta = 0, 0, 0  

'''

m_1 = 

m_2 = 

l_1, l_2, l_3 = 0, 0, 0

for i in range(n_users_floor * n_floors):

    k = w * np.log10(carrier_frequency) + g1 + g2 + g4 * distance_2d_user_drone

    l_1 += w * np.log10(distance_drone_user) + g3 * (1 - math.cos(theta_users[i])) ** 2

    l_2 += w * np.log10(distance_drone_user) + g3 * (1 - math.cos(theta_users[i])) ** 2 + k 

L_total = l_1 + l_2 + l_3
'''