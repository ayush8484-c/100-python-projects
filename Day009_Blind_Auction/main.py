import os
logo = [r'''             
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
''']


print(logo[0])


def highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""

    for bidder in bidding_dictionary:
        bid_price = bidding_dictionary[bidder]

        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = bidder

    print(f"\nThe highest bidder is {winner} with a bid of ${highest_bid}")

bids = {}

continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    bids[name] = price

    choice = input("Are their any other bider? Type 'Yes' or 'No': \n").lower()
    if choice == 'no':
        continue_bidding = False
        highest_bidder(bids)
    elif choice == 'yes':
        print("\n" * 50)
