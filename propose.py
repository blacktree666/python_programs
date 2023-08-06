import colorama
from colorama import Fore
import time
colorama.init(autoreset=True)
print("\n")
for row in range(7):
    for col in range(5):
        if row==0 or col==2 or row==6:
            time.sleep(0.1)
            print("* ",end="")
        else:
            print(end="  ")
    print()
print("\n")

s=f"{Fore.RED}* "
for row in range(6):
    for col in range(7):
        if(row==0 and col%3!=0):
            time.sleep(0.1)
            print(s,end="")
        elif(row==1 and col%3==0):
            time.sleep(0.1)
            print(s,end="")
        elif(row-col==2):
            time.sleep(0.1)
            print(s,end="")
        elif(col+row==8):
            time.sleep(0.1)
            print(s,end="")
        else:
            print(end="  ")
    print()
print("\n")

for row in range(6):
    for col in range(5):
        if((col==0 or col==4)and row<5):
            time.sleep(0.1)
            print("* ",end="")
        elif(row==5 and col>0 and col<4):
            time.sleep(0.1)
            print("* ",end="")
        else:
            print(end="  ")
    print()


    