r = int(input("Enter the number of rows: "))

print("Mirrored right triangle star pattern")
for i in range(1, r + 1):
    for j in range(1, r + 1):
        if (j <= r - 1):
            print('  ', end='  ')
    else:
        print('*',end='  ')
print()