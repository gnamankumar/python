

def count(list):

    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd


lst = [20,14,16,19,21,78,79,26]

even,odd = count(lst)

print("Even : {} and Odd : {}".format(even,odd))
