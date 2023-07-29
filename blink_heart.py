import colorama,time,os,random 
from colorama import Fore 
colorama.init(autoreset=True)
cl=[Fore.RED,Fore.BLUE,Fore.YELLOW,Fore.GREEN]

while True:
    for row in range(6):
        for col in range(7):
            r=random.randint(0,3)
            s=f"{cl[r]}* "
            if(row==0 and col%3!=0):
                print(s,end="")
            elif(row==1 and col%3==0):
                print(s,end="")
            elif(row-col==2):
                print(s,end="")
            elif(col+row==8):
                print(s,end="")
            else:
                print(end="  ")
        print()
    time.sleep(0.5)
    os.system("cls")


