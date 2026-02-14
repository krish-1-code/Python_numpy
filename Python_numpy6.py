#Vector arithmetic
# Vector = Array (+,-,*,/,%) Array
import numpy as np
import math

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([1,2,3,4,5])

sum = arr1 + arr2
diff = arr1 - arr2
prod = arr1 * arr2
div = arr1 / arr2

print(sum)
print(diff)
print(prod)
print(div)


#Given are list of radii array; Find the area of circle using these radii;

radii = np.array([7,14,21,28])

area = math.pi * (radii ** 2)

print(np.round(area,2))