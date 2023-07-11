import time,os,random 
import termcolor as t 
d=["red","blue","green","yellow","cyan"] 
while True:
    for b in d:
        for i in range(10):
            print("\t",end=" ")
            for j in range(10):
                r=random.randint(0,4)
                t.cprint("*",d[r],end=" ")
            print()
        time.sleep(0.5)
        os.system("cls")
        print("\n")


