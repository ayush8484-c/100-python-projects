logo = [ ''' 
                 _____________________
                |  _________________  |
                | | JO           0. | |
                | |_________________| |
                |  ___ ___ ___   ___  |
                | | 7 | 8 | 9 | | + | |
                | |___|___|___| |___| |
                | | 4 | 5 | 6 | | - | |
                | |___|___|___| |___| |
                | | 1 | 2 | 3 | | x | |
                | |___|___|___| |___| |
                | | . | 0 | = | | / | |
                | |___|___|___| |___| |
                |_____________________|    
                   
                ''']

print(logo[0])

def add(n1 , n2):
    return n1 + n2

def sub(n1 , n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1 , n2):
    if n2 == 0:
        return "Error!"
    return n1 / n2



mathematical_operations = {
                            "+": add,
                            "-": sub,
                            "*": mul,
                            "/": div,
                            }

def calculator():
        should_accumulate = True
        num1 = float(input("Enter first number: "))

        while should_accumulate:
                for symbols in mathematical_operations:
                    print(symbols)
                operation = input("Pick an operation: ")
                num2 = float(input("Enter second number: "))

                answer = mathematical_operations[operation](num1, num2)

                print(f"{num1} {operation} {num2} = {answer}")

                choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to stop: ")

                if choice == "y":
                      num1 = answer
                else:
                      should_accumulate = False
                      print("\n" * 20)
                      calculator()


calculator()