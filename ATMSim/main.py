import sys

import mysql.connector

# connect to the data base using mysql-connector-python
mydb = mysql.connector.connect(

    host='localhost',  # host name
    user='root',  # username
    password='Anthony13',  # password
    port='3306',  # SQL port
    database='atm'  # Database to be used
)


def create_db_startup():
    create_db_query = ("DROP SCHEMA IF EXISTS atm;"
                       "CREATE SCHEMA atm;"
                       "use atm;"

                       "CREATE TABLE `account`("
                       "firstName varchar(20) not null,"
                       "lastName varchar(20) not null,"
                       "Balance double not null,"
                       "Pin int not null PRIMARY KEY"
                       ");"

                       "CREATE TABLE accountType("
                       "id int not null, "
                       "accountDescription varchar(20) not null"
                       ");")


def atmSimulator():

    mycursor = mydb.cursor()
    accountMenuChoice = ''

    while True:
        print('         Welcome, Please Choose an Option:       ')
        print('         C - Create an Account')
        print('         L - Login')
        print('         Q - Quit')

        welcomeMenuChoice = input('      Enter your Choice: ')

        # C - Creation of an account
        if welcomeMenuChoice.upper() == 'C':
            firstName = input('        What is your first name?:  ')  # enter first name
            lastName = input('        What is your last name? :')  # enter last name
            while True:  # error checking the first deposit amount to have 1 or more dollars
                try:
                    balance = int(
                        input('        Please enter how much you would like to deposit into your account: '))
                    if balance < 1:
                        balance = int(
                            input('        Please enter how much you would like to deposit into your account: '))
                    else:
                        break
                except ValueError:
                    print('You cannot deposit less than 1 dollar!')

            while True:  # error checking the pin number if longer or shorter than 4 digits
                try:
                    pin = int(input("        Please enter a new 4 digit PIN: "))
                    if len(str(pin)) > 4 or len(str(pin)) < 4:
                        pin = int(input("        Please enter a new 4 digit PIN: "))
                    else:
                        break
                except ValueError:
                    print('Your PIN has to be 4 digits')

            while True:
                print('         Please Choose an Account Option:       ')
                print('         1 - Checking')
                print('         2 - Savings')
                print('         3 - Credit')

                try:
                    acc_type = int(input("        Enter Your Choice: "))
                    if len(str(acc_type)) > 1 or len(str(acc_type)) < 1:
                        print('         Please Enter a Valid Choice:')
                    else:
                        break
                except ValueError:
                    print('Invalid Choice')

            # query to insert values firstname, last name, first deposit and pin into database table
            query_tuple = (firstName, lastName, balance, pin, acc_type)
            query_init = ("INSERT INTO account"
                          "(firstName, lastName, Balance, Pin, typeID)"
                          "VALUES (%s, %s, %s, %s, %s)")
            mycursor.execute(query_init, query_tuple)
            mydb.commit()
            print('Account Successfully Created')

        # L - Logging into an existing account
        if welcomeMenuChoice.upper() == 'L':

            firstName = input('Enter your first name?:  ')
            lastName = input('Enter your last name?: ')
            loginPin = int(input("        Please enter your 4 digit PIN: "))

            query_login_tuple = [loginPin]
            query_login = """select * from account where Pin = %s"""
            mycursor.execute(query_login, query_login_tuple)
            info = mycursor.fetchall()
            tempBalance = 0
            login_account_ID = 0
            for row in info:
                print('ID', row[0])
                login_account_ID = row[0]
                print('FN', row[1])
                print('LN', row[2])
                print('BAL', row[3])
                print('PIN', row[4])
                print('TYPE', row[5])
                tempBalance = row[3]

            print('this is a test ', tempBalance)

            while True:
                print('Confirming Information...')
                try:
                    for pin_num in info:
                        if loginPin == pin_num[4]:
                            print('Success!')
                            break
                except ValueError:
                    sys.exit('Please try again')
                break

            print('   Hello,', firstName, ' Please select an option: ')
            print('         B - Check Balance')
            print('         W - Withdraw')
            print('         D - Deposit')
            print('         P - Change PIN')
            print('         Q - Quit')

            accountMenuChoice = input('     Enter your Choice: ')

            # B - Checking Current Balance Actions
            if accountMenuChoice.lower() == 'b':
                mycursor.execute("select Balance from account where id = %s" % login_account_ID)
                bal_info = mycursor.fetchall()
                for row in bal_info:
                    print('  Your current balance is', row[0])
                    print('  Thank you!')

            # W - Withdraw actions
            if accountMenuChoice.upper() == 'W':
                while True:
                    try:
                        withdraw_amount = int(input("        Please enter an amount to withdraw: "))
                        if withdraw_amount > tempBalance:
                            withdraw_amount = int(input("        Please enter an amount to withdraw: "))
                        else:
                            break
                    except ValueError:
                        print('You cannot withdraw more than your account balance.')

                new_balance = (tempBalance - withdraw_amount)
                print('Your new balance is', new_balance)
                # query to update balance in the database
                mycursor.execute("UPDATE account SET Balance = '%s' WHERE id = '%s'" % (new_balance,login_account_ID))
                mydb.commit()



            # D- Deposit actions
            if accountMenuChoice.upper() == 'D':

                while True:
                    try:
                        depositAmount = int(
                            input('        Please enter how much you would like to deposit into your account: '))
                        if depositAmount < 1:
                            raise Exception
                        else:
                            break
                    except ValueError:
                        print('You cannot deposit less than 1 dollar!')

                new_dep_balance = (tempBalance + depositAmount)
                print('     Your new balance is', new_dep_balance)
                mycursor.execute("UPDATE account SET Balance = '%s' WHERE id = '%s'" % (new_dep_balance, login_account_ID))
                mydb.commit()
            # query to update balance in the database

            # P - Changes Current PIN number.
            if accountMenuChoice.upper() == 'P':
                while True:
                    try:
                        curPin = int(input('        Please enter your current PIN: '))
                        if curPin != loginPin:
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

                mycursor.execute("UPDATE account SET Pin = '%s' WHERE id = '%s'" % (newPin, login_account_ID))
                mydb.commit()

                print('Pin successfully updated!')

            # query to update pin number in db

            # Q- quitting from the login menu
            if accountMenuChoice.upper() == 'Q':
                byeMsg = input('Thank you for using our ATM. Press enter to quit.')
                exit(0)

        # Q - quitting from the welcome menu
        if welcomeMenuChoice.upper() == 'Q':
            byeMsg = input('Thank you for using our ATM. Press enter to quit.')
            exit(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    atmSimulator()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
