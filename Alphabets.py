print("Enter a character: ")
c = input()
if c >='0' and c<='9':
    print("\nIt is an Number")
elif c >='a' and c <='a':
    print("\nIt is an alphabet")
elif c>='A' and c<='Z':
    print("\nIt is an alphabet")
else:
    print("\nIt is neither an alphabet nor a number!")