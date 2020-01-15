import time
from random import randint
import os

def log(func):
    start_time = time.time()
    fd = open("bipbop.txt", "w")
    def fct2(*arg):
         string = "(" + os.getlogin() +")" + " Running: " + func.__name__ + "          "
         string += "[  exec-time = %s  ] \n" % (time.time() - start_time)
         fd.write(string)
         return func(*arg)
    return (fct2)
 
class Filling():
    @log 
    def Plus(self, a):
        self.level += a
        print("Filling Piscine")

    @log 
    def Moins(self):
       print("Oups..")
       return(self.level / 3 * 2)

    @log 
    def Piscine(self):
        self.level = 0
        while self.level < 100:
            a = randint(0,10)
            self.Plus(a)
            if a >= 9:
                self.level += self.Moins()
        print("Piscine ok")
    

tr = Filling()
for i in range(0,5):
    tr.Piscine()

#def log(func):
#    def wrapper():
#        print('call %s():' % func.__name__)
#        return func()
#    return wrapper

#@log
#def now():
#    print('2018-8-28')

#now()
