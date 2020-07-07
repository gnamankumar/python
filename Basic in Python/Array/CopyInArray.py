from numpy import *

arr1 = array([1,2,3,4,5])

#Deep Copy
arr2 = arr1.copy()


#Shallow Copy
#arr2 = arr1.view()

arr1[1] = 7

print(arr1)
print(arr2)

'''
#Output of Deep Copy
[1 7 3 4 5]
[1 2 3 4 5]
'''

'''
#Output Of shallow Copy
[1 7 3 4 5]
[1 7 3 4 5]
'''

#print the adderes pf array
print(id(arr1))
print(id(arr2))
