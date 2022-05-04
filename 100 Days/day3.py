print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
left_or_right = input("You're at a cross road. Where do you want to go? Type 'left' or 'right\n")

if left_or_right == "left":
    print("You came to a lake. There is an island in the middle fo the lake.")
    wait_or_swim = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if wait_or_swim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. ")
        three_doors = input("One red, one yellow and one blue. Which color do you choose? \n")
        if three_doors == "red":
            print("You were assasinated by ninjas. Game Over.")
        elif three_doors == "yellow":
            print("You found the treasure! Congratulations!")
        elif three_doors == "blue":
            print("You fell in an ocean full of sharks. Game Over.")
    else:
        print("You forgot you didn't know how to swim so you drowned. Game Over.")
else:
    print("You have arrived at a desert. What is the first thing you do?")
    water_or_continue = input("Type 'water' to search for water or 'continue' to continue searching for treasure\n")
    if water_or_continue == "water":
        print("You found water and didn't die of thirst. There is a pyramid with 3 levers. \n")
        lever = input("Which lever do you pull? Type 1, 2 or 3\n")
        if lever == 1:
            print("You fell inside a trap and died. Game Over.")
        elif lever == 2:
            print("Your found the treasure! Congratulations!")
        else:
            print("You set free a giant monster. Game Over.")
    if water_or_continue == "continue":
        print("A human can't survive without water for more than 3 days. You died. Game Over.")

