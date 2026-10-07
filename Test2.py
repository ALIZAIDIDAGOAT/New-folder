def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print("😂 MY AWESOME CALCULATOR 😂")
print("1 = Add")
print("2 = Subtract")
print("3 = Multiply")
print("4 = Divide")

try:
    choice = input("Pick a number (1-4): ")

    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    if choice == "1":
        print("Answer:", add(num1, num2))

    elif choice == "2":
        print("Answer:", subtract(num1, num2))

    elif choice == "3":
        print("Answer:", multiply(num1, num2))

    elif choice == "4":
        print("Answer:", divide(num1, num2))

    else:
        print("Bro... pick 1, 2, 3 or 4 😭")

except ZeroDivisionError:
    print("You can't divide by zero bro 💀")

except ValueError:
    print("That's not a number bro 😭")
