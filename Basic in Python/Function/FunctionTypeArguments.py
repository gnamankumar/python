Actual Arguments has 4 types:-1.Position,2.Keyword,3.Default,4.Variable length

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
