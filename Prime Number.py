num = int(input("Enter a number: "))
x = False
for i in range(2,num):
    if num%i == 0:
        x = True
if x == True:
    print("It is a composite Number.")
else:
    print("It is a prime Number.")
