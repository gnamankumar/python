

a=10
print(id(a))
def something():

    a = 15
    x = globals()["a"]
   
   #local variable (Always give prefrence local ver)
    print(id(x))
    print("in fun ",a)


    globals()['a'] = 11

something()



print("outside",a)


#Output
'''
1703278656
1703278656
in fun  15
outside 11
'''
