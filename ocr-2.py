from letters import *

def show_symbol(data):
    for row in data:
        for col in row:
            if col:
                print("⬜ ", end="")
            else:
                print("⬛ ", end="")
        print()

for el in data:
    show_symbol(el)
    print()





