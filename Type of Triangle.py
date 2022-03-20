side_1 = int(input("Enter the units of first side... "))
side_2 = int(input("Enter the units of second side... "))
side_3 = int(input("Enter the units of third side... "))

if side_1 == side_2 == side_3:
    print("It is an equilateral triangle.")

elif side_1 != side_2:
    if side_1 != side_3:
        print("It is a scalene triangle.")
    else:
        print("It is an isoceles triangle.")

else:
    print("It is an isosceles triangle.")
