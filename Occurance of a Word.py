x = [input("Enter a string to check how many times a word is repeated... \nInsert here: ")]
tmp = (x[0].split())
y = input("Enter a substring to check how many times it is repeated... \nInsert here: ")
count = 0
for i in tmp:
    if i == y:
        count += 1
print(y, "occurs",count, "times.")
