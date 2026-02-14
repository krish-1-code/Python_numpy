# Aggregate Functions:
# Summarizing the array of data and typically returning a single variable

import numpy as np

Marks = np.array([82,34,67,42,78,100])

avg_score = np.mean(Marks)
std_deviation = np.std(Marks)
Total = np.sum(Marks)
Variant = np.var(Marks)
Min_marks = np.min(Marks)
Max_marks = np.max(Marks)
Index_ofmax = np.argmax(Marks)
Index_ofmin = np.argmin(Marks)

print(f"Total student = {np.size(Marks)}")
print(f"The total is {Total}.")
print(f"The Average marks is {np.round(avg_score,2)}.")
print(f"The Standard Deviation is {np.round(std_deviation,2)}")
print(f"The Variant is {np.round(Variant,2)}")
print(f"The Lowest mark is {Min_marks}")
print(f"The highest mark is {Max_marks}")
print(f"The index of lowest mark is {Index_ofmax}")
print(f"The index of highest mark is {Index_ofmin}")

#Let's consider a 2-D array 

darray =  np.array([[1,2,3,4,5],
                   [6,7,8,9,10]])

print(np.sum(darray, axis = 0))
print(np.sum(darray, axis = 1))