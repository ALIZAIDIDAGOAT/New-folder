import random
playing = True
number = str(random.randint(5,15))

print("I will generate a number form 5 to 15, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")

while playing:
    guess = input("Type in your most favourite Numbers!")
    if number == guess:
        print("You win the game!")
        print("The numbear was: ", number)
        break
    else:
        print("Try again! You got this pal!")

        print("..................................................................................")

        import random
actions = ["rock","paper","scissors"]
print("You got:", random.choice(actions))

print("...............................................................................................")

import math

print('The floor and Ceiling value of 23.56 are: ' + str(math.ceil(23.56)) + ' , ' + str(math.floor(23.56)))

x = 10
y = -15

print('The value of x after copying the sign from y is: ' + str(math.copysign(x, y)))

print('Absolute value of -96 and 56 are: ' + str(math.fabs(-96)) + ' , ' + str(math.fabs(56)))

print('The GCD of 24 and 56 : ' + str(math.gcd(24, 56)))