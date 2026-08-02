import logo
import resources

print(logo.logo[0])
money = 0

def resource_report(ingredients):
    for item in ingredients:
        if ingredients[item] > resources.resource[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def payment():
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction_successful(money_received, order_cost):
    if money_received >= order_cost:
        change = round(money_received - order_cost, 2)
        global money
        money += order_cost
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry, That's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources.resource[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} ☕")

while True:
    customer_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_order == "off":
        break

    elif customer_order == "report":
        print(f"Water: {resources.resource['water']}ml")
        print(f"Milk: {resources.resource['milk']}ml")
        print(f"Coffee: {resources.resource['coffee']}g")
        print(f"Money: ${money}")

    else:
        drink = resources.menu[customer_order]
        if resource_report(drink["ingredients"]):
            transaction = payment()

            if transaction_successful(transaction, drink["cost"]):
                make_coffee(customer_order, drink["ingredients"])




