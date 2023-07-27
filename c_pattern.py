import colorama 
from colorama import Fore 
colorama.init(autoreset=True)

for row in range(7):
    for col in range(6):
        if(col==0 and (row!=0 and row!=6)) or ((row==0 or row==6) and col>0):
            print(Fore.RED+"C",end=" ")
        else:
            print(end=" ")
    print()
