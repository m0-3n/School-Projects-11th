num = int(input("Enter a number to find it's factorial: "))
fact = 1

if num < 0:
    print("No factorial for negative numbers.")

elif num == 0:
    print("Factorial of 0 is 1.")

elif num > 0:
    for i in range(1,num + 1):
        fact = fact * i
    print(fact, "is the factorial of", num)
