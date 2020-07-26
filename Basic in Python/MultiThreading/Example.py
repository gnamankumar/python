from time import sleep  #because we want to print simultaneously both(Hello,Hi)
from threading import *

class Hello(Thread): #first thread
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)



class Hi(Thread): #second thread
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")

'''
OUTPUT
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Bye
'''
