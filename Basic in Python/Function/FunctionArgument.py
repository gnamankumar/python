

def update(lst):
    
    print(id(lst))


    x = 8
    print(id(lst))
    print("x",lst)

lst = [10,20,30]
print(id(lst))
update(lst)
print("lst",lst)
