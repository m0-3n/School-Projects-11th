x = int(input("Enter the number of rows you want... "))
for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()