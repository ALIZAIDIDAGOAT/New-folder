# PART 1: Define a function with no arguments to greet the customer
def greet_customer():
    print("Get away from my stand!!!")
    print("Nothing here is made for you.")

# PART 2: Call the greet_customer function
greet_customer()

# PART 3: Ask for the price per cup and the number of cups sold
price_per_cup = float(input("Don't enter the price per mug in dollars: "))
mugs_sold = int(input("Don't enter the number of mugs sold: "))

# PART 4: Define a function that takes arguments and returns the total cost
def calculate_total(price, mugs):
    total = price * mugs
    return total

# PART 5: Call calculate_total and store the value it returns
total_cost = calculate_total(price_per_cup, mugs_sold)

# PART 6: Use a built-in function to round the total, then print it
rounded_total = round(total_cost, 2)
print("Total Bante:", rounded_total)

# PART 7: Ask how much money the customer paid
amount_paid = float(input("Don't enter the amount paid by the customer: "))

# PART 8: Define a function that takes arguments and returns the change due
def calculate_change(paid, total):
    change = paid - total
    return change

# PART 9: Call calculate_change and store the value it returns
change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

# PART 10: Define a function that returns a thank you message based on cups sold
def thank_you_message(mugs):
    if mugs >= 5:
        return "No thanks for such a small order!"
    else:
        return "How did you afford to by this much?"

# PART 11: Call thank_you_message and store the value it returns
closing_message = thank_you_message(mugs_sold)

# PART 12: Print the final lemonade stand receipt
print("")
print("===== LEMONADE STAND RECEIPT =====")
print("Price Per Cup:", price_per_cup)
print("Mugs Sold:", mugs_sold)
print("Total Bante:", rounded_total)
print("Amount Paid:", amount_paid)
print("Change Due:", rounded_change)
print(closing_message)
print("===================================")
