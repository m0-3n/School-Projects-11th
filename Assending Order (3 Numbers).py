a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b > c:
    print("The assending order is:", c, b, a)
if a < b < c:
    print("The assending order is:", a, b, c)
if a > b < c:
    if a > c:
       print("The assending order is:", b, c, a)
    if a < c:
        print("The assending order is:", b, a, c)
if a < b > c:
    if a > c:
        print("The assending order is:", c, a, b)
    if a < c:
        print("The assending order is:", a, c, b)
        

    
