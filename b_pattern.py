import colorama 
from colorama import Fore 
colorama.init(autoreset=True) 


for row in range(7):
    for col in range(5):
        if col == 0 or (row == 0 or row == 3 or row == 6) and (col < 4) or col == 4 and (row == 1 or row == 2 or row == 4 or row == 5):
            print(Fore.GREEN+"B ",end="")
        else:
            print(" ",end=" ")
    print()


# this is the python program to print B pattern with green color
