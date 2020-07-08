


def person(name, **data):

    print(name)
   # print(data)

    for i,j in data.items():
        print(i,j)
    


person('naman',age=28,city='Delhi',mob=969090)
