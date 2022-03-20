x = int(input("Enter the bill amount... "))
if x > 100:
    if x < 500:
        print("You get a 15% discount in your final bill.\n")
        print("You're final bill amounts to ", x - (15/100)*x)
    else:
        print("You get a 20% discount in your final bill.\n")
        print("You're final bill amounts to ", x - (20/100) * x)
else:
    print("You get a 5% discount in your final bill.\n")
    print("You're final bill amounts to ", x - (5/100) * x)
