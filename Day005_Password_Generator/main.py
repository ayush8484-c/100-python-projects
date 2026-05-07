import random
letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E',
           'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J',
           'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O',
           'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T',
           'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*']

print("Welcome to the Password Generator!")

number_of_letters = int(input("How many letters would you like in your password?\n "))
number_of_symbols = int(input("How many symbols would you like in your password?\n "))
number_of_numbers = int(input("How many numbers would you like in your password?\n "))

password_list = []
for char in range(1, number_of_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, number_of_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, number_of_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ''.join(password_list)
print(f"Your password is: {password}")