#Comaprison operator in numpy array

import numpy as np

gpa = np.array([2.3,3.2,4.0,1.0,2.9])

print(gpa >= 2.5)

gpa[gpa<2.5] = False
print(np.round(gpa,4))