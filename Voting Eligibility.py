input_1 = int(input("What is your age? "))
if input_1 >= 18:
    print("You are eligible for election, Please vote for the best party.")
else:
    a = 18 - input_1
    print("You are too small to vote, come back after", a, "years.")