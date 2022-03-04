'''
(3/3) Script for the Advanced LED Show
Nathan Tardy - 2.15.2022
Technology and Engineering II - Bangor High School
'''

# Importing necessary libraries
import threading as th

# Defining functions to be used in the threading
def timer(): 
    import timerScriptNTardy

def RGB():
    import RGBScriptNTardy

# Using threading to run the programs simeltaneously
timer = th.Thread(target = timer).start() 
th.Thread(target = RGB).start()
