\from math import sqrt


print("For the Quadratic Equation 'ax^2 + bx + c = 0', enter its coefficients...")
while True:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    if a == 0:
        print("The value of 'a' cannot be ZERO")
    else:
        break

discriminant = b**2 + 4 * a * c

if discriminant > 0:
    root_1 = (-b + sqrt(discriminant)) / (2 * a)
    root_2 = (-b - sqrt(discriminant)) / (2 * a)
    print("There are two real and distinct roots...")
    print("The roots of the equation are,", root_1, "&", root_2)

elif discriminant == 0:
    root_1 = (-b) / (2 * a)
    print("There are two real and equal roots...")
    print("The roots of the equation are,", root_1, "&", root_1)

elif discriminant < 0:
    print("The roots are Imaginary and complex...")
