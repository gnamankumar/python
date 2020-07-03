from numpy import *

#ones
arr = ones(5,int)

#zeros
arr = zeros(5)

#logspace
arr = logspace(1,40,5)

#arange
arr = arange(1,15,2)

#linespace
arr = linspace(0,15,20)

#check array datatype
arr = array([1,2,3,4,5.0],int)

print(arr.dtype)

print(arr)
