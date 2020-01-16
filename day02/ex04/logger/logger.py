# -*- coding: utf-8 -*-

import time
import os

def log(func):
    start_time = time.time()
    fd = open("log_result.txt", "w")
    def fct2(*arg):
         string = "(" + os.getlogin() +")" + " Running: " + func.__name__ + "          "
         string += "[  exec-time = %s  ] \n" % (time.time() - start_time)
         fd.write(string)
         return func(*arg)
    return (fct2)
