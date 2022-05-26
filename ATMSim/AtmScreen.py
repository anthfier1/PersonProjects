import mysql.connector

# connect to the data base using mysql-connector-python
mydb = mysql.connector.connect(

    host='localhost',  # host name
    user='',  # username
    password='',  # password
    port='3306',  # SQL port
    database='atm'  # Database to be used
)


def atmSimulator():
    mycursor = mydb.cursor()

    while True:
        print('         Welcome, Please Choose an Option:       ')
        print('         C - Create an Account')
        print('         L - Login')
        print('         Q - Quit')

    welcomeMenuChoice = input('      Enter your Choice: ')

    # C - Creation of an account
    if welcomeMenuChoice.upper() == 'C':
        firstName = input('What is your first name?:  ')  # enter first name
        lastName = input('What is your last name? :')  # enter last name
        while True:  # error checking the first deposit amount to have 1 or more dollars
            try:
                firstDeposit = int(
                    input('        Please enter how much you would like to withdraw from your account: '))
                if firstDeposit < 1:
                    raise Exception
                else:
                    break
            except ValueError:
                print('You cannot deposit less than 1 dollar!')

        while True:  # error checking the pin number if longer or shorter than 4 digits
            try:
                initPin = int(input("        Please enter a new 4 digit PIN: "))
                if len(str(initPin)) > 4 or len(str(initPin)) < 4:
                    raise Exception
                else:
                    break
            except ValueError:
                print('Your PIN has to be 4 digits')

        # query to insert values firstname, last name, first deposit and pin into database table
        queryInit = 'INSERT INTO account (firstName, lastName, Balance, pin, Account_type_ID) values(', firstName, lastName, firstDeposit, initPin, ');'
        mycursor.execute(queryInit)

    # L - Logging into an existing account
    if welcomeMenuChoice.upper() == 'L':
        firstName = input('Enter your first name?:  ')
        lastName = input('Enter your last name? :')
        loginPin = int(input('Please enter your 4 digit PIN number: '))

        # query to get values from the database table
        # compare the values to each other
        # if true go to next prompt

        print('         Hello,', firstName, ' Please select an option: ')
        print('         B - Check Balance')
        print('         W - Withdraw')
        print('         D - Deposit')
        print('         P - Change PIN')
        print('         Q - Quit')

        accountMenuChoice = input('      Enter your Choice: ')

        # B - Checking Current Balance Actions
        if accountMenuChoice.upper == 'B':
            balance = ''  # query to get the balance and then print to the screen
            print('     Your Current Balance is: ', balance)

        # W - Withdraw actions
        if accountMenuChoice.upper() == 'W':
            tempBalance = int('')  # query to get the balance store it
            while True:
                try:
                    withdrawAmount = int(
                        input('        Please enter how much you would like to withdraw from your account: '))
                    if withdrawAmount > tempBalance:
                        raise Exception
                    else:
                        break
                except ValueError:
                    print('You cannot withdraw more than your balance!')

            newBalance = (tempBalance - withdrawAmount)
            print('Your new balance is', newBalance)
            # query to update balance in the database

        # D- Deposit actions
        if accountMenuChoice.upper() == 'D':
            tempBalance = int('')  # query to get the balance store it
            while True:
                try:
                    depositAmount = int(
                        input('        Please enter how much you would like to withdraw from your account: '))
                    if depositAmount < 1:
                        raise Exception
                    else:
                        break
                except ValueError:
                    print('You cannot deposit less than 1 dollar!')

            newBalance = (tempBalance + depositAmount)
            print('     Your new balance is', newBalance)
            # query to update balance in the database

        # P - Changes Current PIN number.
        if accountMenuChoice.upper() == 'P':
            tempPin = int('')  # query to get the existing PIN Number for the account

            while True:
                try:
                    curPin = int(input('        Please enter your current PIN: '))
                    if curPin != tempPin:
                        raise Exception
                    else:
                        break
                except ValueError:
                    print('     The PIN you have entered does not match the account PIN')

            while True:
                try:
                    newPin = int(input("        Please enter a new 4 digit PIN: "))
                    if len(str(newPin)) > 4 or len(str(newPin)) < 4:
                        raise Exception
                    else:
                        break
                except ValueError:
                    print('Your PIN has to be 4 digits')

            # query to update pin number in db

        # Q- quitting from the login menu
        if accountMenuChoice.upper() == 'Q':
            byeMsg = input('Thank you for using our ATM. Press enter to quit.')
            exit(0)

    # Q - quitting from the welcome menu
    if welcomeMenuChoice.upper() == 'Q':
        byeMsg = input('Thank you for using our ATM. Press enter to quit.')
        exit(0)
