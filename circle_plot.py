# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 18:03:30 2024

@author: 1
"""

import math as m 
import matplotlib.pyplot as plt
import numpy as np

r = 3
X = 12
Y = 12 


x = []
y = []

for i in np.arange(0,365,0.1):
    
    x.append(r * m.cos(i) + X)
    y.append(r * m.sin(i) + Y)
    
    
plt.plot_date(x, y,'.')

plt.show()