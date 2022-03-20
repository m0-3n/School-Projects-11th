x = input("Enter a string to check if it is a palindrome... ")
if x == x[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
