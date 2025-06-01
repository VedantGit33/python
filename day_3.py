#Create 1D array using arange() and convert that 1D array
#to 3D array

#Create an array with random numbers
#Create a function to find area of circle using return statement.
#Write a code to generate 10 random integers between 1 to 100?
#Create 1D array of 25 numbers. Change it to a 2D array



''' 1. 1D array to 3D array. '''

'''import numpy as np

arr_1D = np.arange(1,7)
print(arr_1D)

arr_3D = arr_1D.reshape(3,1,2)
print(arr_3D)'''

''' 2.  Create an array with random numbers'''

'''import random

a = random.randint(1,10)
print(a)'''



''' 3. Create a function to find area of circle using return function.'''

def area_circle(r):
    pi = 3.14
    area = pi*r**2

    return area

print("Area of Circle:",area_circle(12))

