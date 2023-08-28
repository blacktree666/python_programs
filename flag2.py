import colorama,time 
from colorama import Fore 
colorama.init(autoreset=True) 
print("\n"*5)

for row in range(3):
    for col in range(35):
        time.sleep(0.01)
        print(Fore.RED+"*",end="")
    print()

for row in range(3):
    for col in range(35):
        time.sleep(0.01)
        print("*",end="")
    print()

for row in range(3):
    for col in range(35):
        time.sleep(0.01)
        print(Fore.GREEN+"*",end="")
    print()


print("\n"*5)
