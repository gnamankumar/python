#First Program which save name is (Demo.py)
from calc import add

def func1():
      add()
      print('From Function1')
def func2():
      print('From Function2')

def main():
      func1()
      func2()
main()
Output:
result 1 is calc
From Function1
From Function2

#Second Program which save name is (calc.py)
def add():
      print('result 1 is',__name__) #We use this because we wanna access only add function in (Demo.py)
def sub():
      print('result 2 is')
def main():
      print('in Calc main')
      add()
      sub()
if __name__=='__main__': #Because of this we only call only add function in demo.py 
      
      main()
      
Output:-
in Calc main
result 1 is __main__
result 2 is
