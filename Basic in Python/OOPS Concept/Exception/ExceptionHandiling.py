#ERROR 3 TYPES:-Compile time error(missing (:)in a program),Logical error(Wrong Output),Run time error(code not give logical,compile time error in [eg.divide by zero])
#EXCEPTION HANDLING

a = 5
b = 2

try:
    print("resource Open")
    print(a/b)
    k = int(input("Enter a number"))5
    print(k)

except ZeroDivisionError as e:
    print("Hey ,You can not divide a Number by Zero", e)
    
except ValueError as e:
    print("Invalid Error")

except Exception as e: #Exception is handling every type of error
    print("Some errror...")

finally: #Finally block will be executed if we get error as well as if we don't get the error.
    print("resource Closed")

#OUTPUT
    '''
 resource Open
2.5
Enter a numberp
Invalid Error
resource Closed'''
