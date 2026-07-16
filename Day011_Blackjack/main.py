import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Calculates the score of a hand."""

    # Blackjack (Ace + 10-value card)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Convert Ace from 11 to 1 if score is over 21
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    """Determines the winner."""

    if user_score == computer_score:
        return "🤝 Draw!"

    elif user_score == 0:
        return "🎉 You win with a Blackjack!"

    elif computer_score == 0:
        return "💻 Computer wins with a Blackjack!"

    elif user_score > 21:
        return "💥 You went over 21. You lose!"

    elif computer_score > 21:
        return "🎉 Computer went over 21. You win!"

    elif user_score > computer_score:
        return "🎉 You win!"

    else:
        return "💻 You lose!"


user_cards = []
computer_cards = []
game_over = False

# Deal two cards each
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print("\n----------------------------")
    print(f"Your cards: {user_cards}")
    print(f"Your score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        choice = input("Type 'y' to get another card or 'n' to pass: ").lower()

        if choice == "y":
            user_cards.append(deal_card())
        else:
            game_over = True

# Computer draws until score is at least 17
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print("\n========== FINAL RESULT ==========")

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

print(compare(user_score, computer_score))