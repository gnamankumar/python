'''

def person(name,age=18):
    print(name)
    print(age)



person('naman',22)
'''

#Varible Length

def sum(a, *b):

    c = 0

    for i in b:
        c = c+i

        
    print(c)
    
sum(5,6,34,78)
