
nums = [3,2,3,4,5,8,6,7,5]

#filter is a in built function in python


evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n : n*2,evens))


print(doubles)
print(evens)
