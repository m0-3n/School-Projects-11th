x = input("Enter a number to find the sum of their digits... ")
sum_1 = 0
for i in x:
    i = int(i)
    sum_1 += i
print("The sum of the digits", x, "is:", sum_1)
