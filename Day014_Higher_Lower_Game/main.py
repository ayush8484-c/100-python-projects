import random
import game_data
import logo

print(logo.logo[0])

def check_answer(guess, person_a, person_b):
    follower_a = person_a["follower_count"]
    follower_b = person_b["follower_count"]

    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_over = False

person_a = random.choice(game_data.data)
person_b = random.choice(game_data.data)
while person_a == person_b:
      person_b = random.choice(game_data.data)

while not game_over:
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
    print(logo.VS[0])
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    while guess not in ["a", "b"]:
        guess = input("Please type only 'A' or 'B': ").lower()

    result = check_answer(guess, person_a, person_b)

    if result:
        score += 1
        print(f"You are correct! Current score: {score}")

        person_a = person_b
        person_b = random.choice(game_data.data)

        while person_a == person_b:
            person_b = random.choice(game_data.data)

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True



