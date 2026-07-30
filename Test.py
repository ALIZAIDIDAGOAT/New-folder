secret = 27
attempts = 5

while attempts > 0:
    guess = int(input("Enter the number you want to guess(1-50): "))
    if guess== secret:
     print("You won!!!😎")
     break

    diff = abs(secret - guess)

    if diff >= 20:
       print("Ice cold 🧊")
    elif diff >=10:
       print("Cold 🧊")
    elif diff >=5:
       print("Warm🌶️")
    else:
       print("HOT🔥")

       attempts -= 1

       print("Lives left:", end=" ")
       for i in range(attempts):
          print("💘", end="")
          print()

          if attempts == 0:
             print("You Lost!")
             print("The secret number was: ", secret)