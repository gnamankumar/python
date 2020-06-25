x = int(input("Enter the value ->")) 

r = x % 2

if r==0:
    print("Even")
    if x>5:
        print("Great")
    else:
        print("Not Great")
# When the if condition is inside the if it is called inside if

else:
    print("Odd")



print("Bye")
