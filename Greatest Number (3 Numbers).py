a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
c = int(input("enter 3rd number: "))

if a < b:
    if b < c:
        print(c, "is the greatest")
    elif b > c:
        print(b, "is the greatest")

elif a > b:
    if a < c:
        print(c, "is the greatest")
    elif a > c:
        print(a, "is the greatest")

elif a == b and b == c:
    print("The numbers are all equal.")