x = input("Enter a string to find how many vowels, numbers, uppercase letters, lowercase letters and words...\nEnter:  ")
vow = 0
num = 0
upper = 0
lower = 0
words = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in x:
    for j in vowels:
        if i == j:
            vow += 1
            if i.isupper():
                upper += 1
            if i.islower():
                lower += 1
    if i.isdigit():
        num += 1
    elif i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isspace():
        words += 1

print("There are", vow, "vowels in this string")
print("There are", num, "numbers in this string")
print("There are", upper, "uppercase letters in this string")
print("There are", lower, "lowercase letters in this string")
if x == '':
    print("Enter a String...")
else:
    print("There are", words + 1, "words in this string")
