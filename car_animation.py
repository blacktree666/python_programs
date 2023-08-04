import time,os 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_car(position):
    car = [
        f"{' ' * position}  ______",
        f"{' ' * position} //|_||\\`.__",
        f"{' ' * position}|  _  | ____)/",
        f"{' ' * position}'-(_)-'\\(_) )"
    ]
    for line in car:
        print(line)

def animate_car():
    for i in range(40):
        clear_screen()
        draw_car(i)
        print("---"*20)
        time.sleep(0.1)
def main():
    while True:
        animate_car()

main()
