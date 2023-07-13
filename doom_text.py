import colorama 
from colorama import Fore 
import random,time,os 
colorama.init(autoreset=True) 
c=[Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.RED,Fore.WHITE,Fore.MAGENTA,Fore.CYAN,Fore.LIGHTRED_EX]
a=str(input("\nEnter anythiing:"))
while True:
    time.sleep(0.5)
    os.system("cls")
    if a=="q":
        break 
    print("\n")
    for i in range(len(a)):
        r=random.randint(0,len(c)-1)
        p=f"{c[r]}{a[i]}"
        print(p,end=" ")


