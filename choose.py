#A simple program that makes random decisions for you when you don't want to
#Enter what you want to choose between and the program will choose randomly
#Austin Miller 3/3/13

import random
import time
from sys import stdout

print("Input your options one at a time, followed by the Enter key.\n\
(Enter an empty line at any time and I will select your choice.)\n")

list = []
c = None
count = 1

while c != "":
    c = input("Option "+str(count)+": ")
    if c == "":
        break
    list.append(c.upper())
    count += 1
    
print("\nI will now choose for you...\n")
num = random.randrange(0,len(list))
choice = list[num]

time.sleep(1)
stdout.write("\rYour choice is...")
time.sleep(1)
stdout.write("  "+choice)

time.sleep(1)
input("\n\n\nPress Enter to Exit")
