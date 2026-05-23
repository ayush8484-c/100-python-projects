import random

HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = [
    "apple", "banana", "orange", "grapes", "mango","tiger", "lion", "elephant", "monkey", "rabbit",
    "school", "garden", "window", "pencil", "bottle","mountain", "river", "forest", "desert", "island",
    "rainbow", "thunder", "sunshine", "snowflake", "hurricane","chocolate", "sandwich", "popcorn", "pancake", "noodles",
    "football", "cricket", "tennis", "basketball", "badminton","guitar", "piano", "violin", "drums", "trumpet",
    "holiday", "journey", "adventure", "treasure", "mystery","diamond", "emerald", "crystal", "silver", "golden",
    "butterfly", "peacock", "sparrow", "penguin", "dolphin","castle", "village", "market", "library", "station"
]
hangman_ascii = [ '''
                     HH   HH    AAA    NN   NN   GGGGG   MM   MM    AAA    NN   NN
                     HH   HH   AA AA   NNN  NN  GG       MMM MMM   AA AA   NNN  NN
                     HHHHHHH  AA   AA  NN N NN  GG GGG   MM M MM  AA   AA  NN N NN
                     HH   HH  AAAAAAA  NN  NNN  GG  GG   MM   MM  AAAAAAA  NN  NNN
                     HH   HH  AA   AA  NN   NN   GGGGG   MM   MM  AA   AA  NN   NN
                 ''']

print(hangman_ascii[0])
print("🎮 Welcome to HANGMAN 🎮")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

placeholder = ""
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"*************************{lives}/6 Lives Left*************************")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You guessed it correctly:+ {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter

            if guess not in correct_letters:
                correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " , display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed it incorrectly: {guess}")

        if lives == 0:
            game_over = True
            print("You lost!\n")
            print(f"The correct word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("You won!")

    print(HANGMANPICS[6 - lives])