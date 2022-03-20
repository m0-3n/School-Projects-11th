def checker(str1):
    char = input('Enter a char to check: ')
    count = 0
    str2 = str1.split()
    for i in range(len(str2)):
        if(str2[i] == char):
            count += 1
    print('The total no. of time',char,'Appears in the string is', count)
checker(input('Enter a string: '))

def vow(str2):
    vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for i in str2:
        if i in vowel:
            str2 = str2.replace(i,"*")
    print(str2)
vow(input('Enter a string: '))
