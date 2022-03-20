x = input("Enter a string to get its palindrome...")
if x == x[::-1]:
    print("It is already a palindrome.")
else:
    tmp = x[:-1]
    print("The palindrome of the given string would be:d", x + tmp[::-1])