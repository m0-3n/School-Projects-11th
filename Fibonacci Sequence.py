n = int(input("Enter the number of terms to be displayed of the fibonacci sequence... "))
a = 0
b = 1
print(a, end=' ')
print(b, end=' ')
for i in range(3, n +1):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
