#Tip Calculator
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage of tip would you like to give? 10 12 15: "))
split = int(input("How many people to split the bill? "))
each_person_bill = ((bill + (bill*tip/100))/split)
print(f"Each person should pay: ${each_person_bill:.2f}")