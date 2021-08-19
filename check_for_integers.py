def checkforInt():
    while True:
        try:
            intTarget = int(input('\nPlease enter your number.\n\n'))
        except ValueError:
            print('\nYou have entered an invalid input. Please enter again.\n')
            continue
        else:
            return (intTarget)
            
checkforInt()
