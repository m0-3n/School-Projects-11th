# Program to count specific element in tutple
t = (1,2,3,4,5,5,5,8,9,10)
print("the tuple is:", t)

n = int(input('Enter a number to count: '))
count = t.count(n)
print(n, "is repeated", count, "times.")
