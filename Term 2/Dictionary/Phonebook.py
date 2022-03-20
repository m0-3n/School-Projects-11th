phonebook = {}
while True:
    print("1. Add a record \n2. Search a record \n3. Update a record \n4. Delete a record \n5. Show record \n6. Quit")
    opt = int(input('Enter your choice (1/2/3/4/5/6): ' ))

    if opt == 1:
        name = input('Enter a name')
        number = int(input('Enter the number'))
        if name in phonebook:
            print('record already exists')
        else:
            phonebook[name] = number
            print('Record successfully added')
    elif opt == 2:
        name = input('Enter a name')
        if name in phonebook:
            print(name,':',phonebook[name])
        else:
            print('Record not found')
    elif opt == 3:
        name = input('Enter a name')
        if name in phonebook:
            number = int(input(('Enter the new number: ')))
            phonebook[name] = number
            print('Record Upadated')
        else:
            print('Record nnot found')
    elif opt == 4:
        name = input('Enter a name: ')
        if name in phonebook:
            del(phonebook[name])
        else:
            print('Record not found')
    elif opt == 5:
        print("The Phone book is:\n", phonebook)
    elif opt == 6:
        break
    else:
        print("\nGive a valid input")

