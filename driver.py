"""
Creator:    Ananda Irwin
Purpose:    Driver file for the tycoon game.
Updated:    10/13/2024
"""

from product import *
from store import *
import time

run_program = True
print("\nWelcome to your very own Mall Planner! Add stores, items, and more!")
mall_name = input("\nFirst, let's start off with a name! It needs to be something catchy.\t")
print("\nHmm.", end = "")

for i in range(0, 3):
    time.sleep(0.75)
    print(".", end = "")

print("\n\n" + mall_name + ", eh? That sounds great! Let's begin:")

while run_program:

    print("\nActions:")
    print("1)\tCreate New Store\n2)\tEdit Existing Store\n3)\tLoad Data From File\n4)\tSave Data To File")
    user_option = int(input("Choose option 1-4:\t"))
    while 4 < user_option < 1:
        user_option = input("Invalid choice. Must type a number 1-4:\t")

    match user_option:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 3:
            pass



    run_program = False