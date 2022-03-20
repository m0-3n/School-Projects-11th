x = int(input("Enter a number to check if it is an Armstrong\'s Number... "))
x = str(x)
tmp = 0
for i in x:
    i = int(i)
    tmp += pow(i, 3)

if x == str(tmp):
    print("It is an Armstrong\'s Number.")
else:
    print("It is not an Armstrong\'s Number.")
