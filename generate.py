"""
display 3d data.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# load data
data = pd.read_csv("output/result.csv")
# print(type(data), data)

for index, item in data.iterrows():
    ax.scatter(float(item['x']), float(item['y']),
               float(item['z']), marker='o', c='r')
ax.set_xlabel('Activity Degree')
ax.set_ylabel('Interaction Diversity')
ax.set_zlabel('Interaction Density')

plt.show()
