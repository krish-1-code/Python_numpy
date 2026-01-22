#Multidimensional array/list in numpy

#Let's first create a 1 dimensional array

import numpy as np

array1 = np.array([1,2,3,4,5])

for i in array1:
    print(i,end = " ")
print()
print(f"Dimension of array is {array1.ndim}")
print()


#Now, let's create a 2 dimensional array

array2 = np.array([[1,2,3],
          [4,5,6],
          [7,8,9]])

for i in array2:
    for j in i:
        print(j, end = " ")
    print()
print()
print(f"Dimension of the array: {array2.ndim}")
print()


#Now, lets print a 3D array

array3 = np.array([[[1,2,3],[4,5,6],[7,8,9]],
          [['a','b','c'],['d','e','f'],['g','h','i']],
          [[10,11,12],[13,14,15],[16,17,18]]])

for i in array3:
    for j in i:
        for k in j:
            print(k,end = " ")
        print()
    print()
print()
print(f"Number of dimensions: {array3.ndim}")
#print(array3.size)

#Let's say we have to access an index in the 3d array 
#Either we can:

print(array3[0][1][2]) #this is called cahin indexing

#Or we can

print(array3[0,1,2]) #This is called multi dimensional indexing It's faster than chain indexing

#Based on the arrays elements we can concatenate to form a string 

word = array3[1,1,1] + array3[1,2,0] + array3[2,0,1]

print(word)
