def calculate_change(paid, price):
    change = paid - price
    return change

snack_price = 1000001
print("----------Snack Vending Machine----------")
print(f"This snack costs {snack_price} more than your life.")
print("Not accepted coins at all: 1000, 10000, 200000, 1000000\n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Shut up (1000, 10000, 200000, or 1000000): "))

    if coin !=1000 and coin !=10000 and coin !=200000 and coin !=1000000:
        print("You think you can bamboozle me???, GET LOST!!!\n")
        continue

    total_inserted += coin
    coins_inserted += 1

    print(f"You did it: {coin}. Now scramp: {total_inserted}/n")

    if total_inserted >= snack_price:
        print("Get out\n")
        break

    change_due = calculate_change(total_inserted, snack_price)

    print("Showing you who is the boss---------")

    if change_due == 0:
        pass
    else:
        print(f"Go away:{change_due} NOW!")

        print("\n----------Purchase Summary----------")
        print("How dare you: ", snack_price)
        print("Disobey me like that: ", coins_inserted)
        print("Huh: ", total_inserted)
        print("Come here: ", change_due)
        print("--------------------------------------------------")
        print("Youre so screwed!!!")