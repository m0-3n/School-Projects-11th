# Code to count number of vowels in a string.

def vowcount(string):
    vowel_counter = 0
    vowel_words = []
    vowels = ["a", "e", "i", "o", "u"]
    upper_vowels = [c.upper() for c in vowels]

    for word in string.split():
        if word[0] in vowels or word[0] in upper_vowels:
            vowel_counter += 1
            vowel_words.append(word)

    print(f"Vowel Words: {len(vowel_words)}")

vowcount(input("Enter a string: "))

