try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma: "))
    result = num1 / num2
    print("The result is: ", result)

except ZeroDivisionError:
 print("Division by zero is error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

except SyntaxError:
   print("Comma is missing. Enter numbers separated by commas like this 1, 2, 3")

except:
   print("Wrong Input!")

else: print("No Exceptions!!!")

finally:
   print("This will execute wether you want it or not!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")