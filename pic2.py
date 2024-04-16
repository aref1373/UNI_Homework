# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 03:22:43 2024

@author: aref
"""


import numpy as np



a = np.zeros((10,10))

d_table = a.copy()
d_table2 = a.copy()

x1 = 9
y1 = 9 
a[y1][x1] = 2

x2 = 0
y2 = 2
a[y2][x2] = 2


# دو نقطه‌ی داده شده
#point1 = (x1, y1)
#point2 = (x2, y2)

# # استخراج مختصات x و y از نقاط
# x_coords, y_coords = zip(point1, point2)
# # ساخت ماتریس A برای رگرسیون خطی
# A = np.vstack([x_coords, np.ones(len(x_coords))]).T
# # حل معادله‌ی خطی با استفاده از رگرسیون خطی
# m, c = np.linalg.lstsq(A, y_coords, rcond=None)[0]
# # نمایش معادله‌ی خطی
#print(f"معادله‌ی خطی: y = {m:.2f}x + {c:.2f}")


def get_linear_equation():
    # Extract coordinates from the given points
    #x1, y1 = point1
    #x2, y2 = point2
    
    # Calculate the slope (m) using the difference in y-coordinates and x-coordinates
    m = (y2 - y1) / (x2 - x1)
    
    # Calculate the y-intercept (c) using one of the points
    c = y1 - m * x1
    
    # Return the linear equation in the form y = mx + c
    
    return m,c


m,c = get_linear_equation()

print('linear_equation is :')
print(f'Y = {m:.1f} x + {c:.1f}')

j = abs(x2 - x1)
min_ = min(x1, x2)

for i in range(1,j):
    
    x = min_ + i
    y = round(m * x + c)
    a[y][x] = 1
    
print (a)