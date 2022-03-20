x = input("Enter a sentence to check how many words are there... ")
count = 0
for i in x:
    if i.isspace():
        count += 1
print("The number of words are", count + 1)