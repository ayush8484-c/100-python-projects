import random

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = ''' 
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissors = '''  
Scissors 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
if user_choice < 0 or user_choice > 2:
  print("You chose an invalid number.")
else :
    print("You chose:")
    print(game_image[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_image[computer_choice])

    if computer_choice == user_choice:
        print("Match Draw!!")
    elif computer_choice == 2 and user_choice == 0:
        print("You Win!!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!!")
    elif computer_choice > user_choice :
        print("You Lose!!")
    else :
        print("You Win!!")
