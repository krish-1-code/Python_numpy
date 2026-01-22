#Lets say we have a list of [1,2,3,4,5] and we want to multiply it by 2. 
#Traditionally we would get [1,2,3,4,5,1,2,3,4,5]
#But if you use numpy lib then you will get [2,4,6,8,10]

import numpy as np

list_num = np.array([1,2,3,4,5])
list_num *= 2
print(list_num)