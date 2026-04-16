print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")
choice_1 = input('You\'re at a crossroads, where do you want to go? Type "left" or "right" ').upper()
if choice_1 == "LEFT":
    print("Congratulations!!!")
    print("You took the right direction")
    choice_2 = input('You have reached at the river bank, you want to "swim" or "wait" ').upper()
    if choice_2 == "WAIT":
        print("Congratulations!!!")
        print("A boat pass nearby helped you cross river safely.")
        choice_3 = input('You get three doors but have to choose one. Which one you are going to choose? "red" "blue" or "yellow"? ').upper()
        if choice_3 == "YELLOW":
            print("Congratulations!!! YOU WON")
        elif choice_3 == "RED":
            print("You burned by fire. Game Over!!!")
        else:
            print("Eaten by beast. Game Over!!!")
    else:
        print("Attacked by trout. Game over!!!")
else:
    print("Fall into a hole. Game over!!!")

