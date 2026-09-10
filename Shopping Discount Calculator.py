# Shopping Discount Calculator
 
valid = False
 
while not valid:
    try:
        # PART 1: Take bill amount, discount percent, and number of people
        bill_amount, discount_purcent, people = input(
            "Enter bill amount, discount purcent, and people separated by commas: "
        ).split(",")
 
        bill_amount = float(bill_amount)
        discount_purcent = float(discount_purcent)
        people = int(people)
 
        # PART 2: Check for invalid values
        if bill_amount <= 0 or discount_purcent < 0 or people < 0:
            raise ValueError
 
        # PART 3: Calculate discount
        discount_amount = bill_amount * discount_purcent / 100
        final_amount = bill_amount - discount_amount
 
        # PART 4: Divide bill between people
        amount_per_person = final_amount / people
 
    except ValueError:
        print("Invalid input! Enter values like this: 1000, 10, 2")
 
    except ZeroDivisionError:
        print("People cannot be 0. Please enter at least 1 person.")
 
    else:
        print("===== SHOPPING DISCOUNT SUMMARY =====")
        print("Original Bill:", bill_amount)
        print("Discount Percent:", discount_purcent)
        print("Discount Amount:", discount_amount)
        print("Final Amount:", final_amount)
        print("Amount Per Person:", round(amount_per_person, 2))
        print("=====================================")
        valid = True
 
    finally:
        print("Discount check completed for this attempt.")
