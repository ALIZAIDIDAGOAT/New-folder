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