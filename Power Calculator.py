num = int(input("Enter the number which you want to reveal the secret power of: "))

pw = int(input("Enter the power: "))

g = 1

for n in range(pw):

    g = g * num

    print(g)