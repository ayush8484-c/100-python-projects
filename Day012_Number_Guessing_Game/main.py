import random

logo = [ r'''
  _____                        _   _             _   _                 _               
 / ____|                      | | | |           | \ | |               | |              
| |  __ _   _  ___  ___ ___   | |_| |__   ___   |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | |_ | | | |/ _ \/ __/ __   | __| '_ \ / _ \  | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |__| | |_| |  __/\__ \__    \ |_| | | |  __/  | |\  | |_| | | | | | | |_) |  __/ |   
 \_____|\__,_|\___||___/___/  \__|_| |_|\___|   |_| \_|\__,_|_| |_| |_|_.__/ \___|_|      
                                                                                          ''']
print(logo[0])

print("Welcome to Number Guessing Game")
print("i'm guessing of a number between 1 and 100")
difficulty = input("Choose a difficulty: easy, medium, hard\n").lower()

comp_num = random.randint(1, 100)

if difficulty == "easy":
    lives = 10
    print(f"You have {lives} lives to guess the correct number")

    while lives > 0:
      guess = int(input("Guess a number: "))

      if guess == comp_num:
          print(f"🎉 Congratulations! You guessed the number {comp_num}.")
          break

      elif guess < comp_num:
          lives -= 1
          print("Guessed number is too low. Try again!")
          print(f"You have {lives} lives left")

      elif guess > comp_num:
          lives -= 1
          print("Guessed number is too high. Try again!")
          print(f"You have {lives} lives left")

    if lives == 0:
        print(f"You ran out of lives! The correct number was {comp_num}.")

elif difficulty == "medium":
    lives = 7
    print(f"You have {lives} lives to guess the correct number")

    while lives > 0:
      guess = int(input("Guess a number: "))
      if guess == comp_num:
          print(f"🎉 Congratulations! You guessed the number {comp_num}.")
          break

      elif guess < comp_num:
          lives -= 1
          print("Guessed number is too low. Try again!")
          print(f"You have {lives} lives left")

      elif guess > comp_num:
          lives -= 1
          print("Guessed number is too high. Try again!")
          print(f"You have {lives} lives left")

    if lives == 0:
        print(f"You ran out of lives! The correct number was {comp_num}.")

elif difficulty == "hard":
    lives = 5
    print(f"You have {lives} lives to guess the correct number")

    while lives > 0:
      guess = int(input("Guess a number: "))

      if guess == comp_num:
          print(f"🎉 Congratulations! You guessed the number {comp_num}.")
          break
      elif guess < comp_num:
          lives -= 1
          print("Guessed number is too low. Try again!")
          print(f"You have {lives} lives left")

      elif guess > comp_num:
          lives -= 1
          print("Guessed number is too high. Try again!")
          print(f"You have {lives} lives left")

    if lives == 0:
        print(f"You ran out of lives! The correct number was {comp_num}.")

else:
    print("Invalid difficulty.")
    exit()