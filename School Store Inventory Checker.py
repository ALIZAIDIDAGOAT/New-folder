items = ['pencil', 'rubber', 'sharpener', 'notebook', 'glue']
stock_counts = [12, 0, 8, 5, 3]

inventory = {item: count for item, count in zip(items, stock_counts)}
print("FULL INVENTORY: ", inventory)

in_stock_items = [item for item in items if inventory[item] > 0]
print("Items in stock: ", in_stock_items)

chosen_item = input("Which item do you want???")

if chosen_item not in inventory or inventory[chosen_item] == 0:

    print(chosen_item,"is out of stock, please come back later!")
    exit()

    prices = [10, 5, 40, 15, 20]
    markup = int(input("Enter markup to add: "))

marked_up_prices = list(map(lambda p : p + markup, prices))
print("Marked up prices: ", marked_up_prices)

items_index = items.index(chosen_item)
chosen_price = marked_up_prices[items_index]
print("Price of", chosen_item, "after markup: ", chosen_price)

inventory[chosen_item] = inventory[chosen_item] - 1
print(chosen_item, "Purchased! Remaining stock: ",inventory[chosen_item])

print("")
print("Schoool store inventory checker")
print("Item bought: ", chosen_item)
print("Price paid: ", chosen_price)
print("Updated inventory: " ,inventory)
print("----------------------------------------------------------------------------------------")