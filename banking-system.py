# LEE CHUN KIT
# TP072511
# LEE CHEE CHENG
# TP072642

from datetime import datetime


# function to read data by column from a file and return it as a list of lists
def getDataByColumn(fileName):
    dataList = []

    with open(fileName, "r") as fileData:
        for record in fileData:
            recordList = record.strip().split(", ")
            dataList.append(recordList)
    return dataList


# function to modify a specific field in the data and save it back to the file
def modifyDetails(fileName, field, data, oldData, newData):
    for index, record in enumerate(data):
        if record[field] == oldData:
            record[field] = newData
            break

    saveData(fileName, data)


# function to save data to a file
def saveData(fileName, data):
    with open(fileName, "w") as destinationFile:
        for record in data:
            recordString = ", ".join(record)
            destinationFile.write(recordString + "\n")


# function to save transaction details to a file
def saveTransaction(accountNumber, transactionAmount, accountBalance, transactionType):
    with open("transaction.txt", "a") as destinationFile:
        transactionDate = datetime.now().strftime("%Y/%m/%d")
        record = [accountNumber, str(transactionAmount), str(accountBalance), transactionDate, transactionType]
        recordString = ", ".join(record)
        destinationFile.write(recordString + "\n")


# function to get customer's account type
def getAccountType(accountNumber):
    # Get list of customer users from the file
    userList = getDataByColumn("customer.txt")

    # loop through each customer user record and find the matching account number
    for record in userList:
        if accountNumber == record[0]:
            accountType = record[9]

            # check and return the account balance limit
            if accountType == 'Savings':
                return 100
            elif accountType == "Current":
                return 500
            else:
                print("\nInvalid account type\n")
                return 0
    else:
        print("\nInvalid account number\n")
        return 0


# function to create a new admin account
def createAdmin(userList=None):
    if userList is None:
        userList = getDataByColumn("admin.txt")

    print("~" * 40)
    print("Admin Account Creation Page")
    print("~" * 40)
    adminUsername = input("Enter a new admin username > ")
    adminPassword = input("Enter a new admin password > ")

    # check if the admin username already exists
    for record in userList:
        if record[0] == adminUsername:
            print("\nThis admin username already exists.\n")
            break
    else:
        # if the username does not exist, add the new admin account
        with open("admin.txt", "a") as destinationFile:
            newRecord = [adminUsername, adminPassword]
            newRecordString = ", ".join(newRecord)
            destinationFile.write(newRecordString + "\n")
        print("\nNew Admin Account has been created.\n")


# Function to create a new customer account
def createCustomer():
    userList = getDataByColumn("customer.txt")
    customerList = []

    print("~" * 40)
    print("Customer Account Creation Page")
    print("~" * 40)

    count = int(input("Enter the number of customer accounts that you want to create > "))

    for i in range(count):
        print(f"\nCustomer #{i + 1}\n")

        # assign an auto generated account number and a default password
        accountNumber = str(1000 + len(userList) + (i + 1))
        customerPassword = "default_password"

        # Input validation for customer name
        while True:
            customerName = input("Name > ")
            if customerName.replace(" ", "").isalpha():
                break
            else:
                print("Invalid name. Please enter a valid name.")

        # Input validation for customer IC
        while True:
            customerIC = input("IC (Example: 030920140813) > ")
            if customerIC.isalnum() and len(customerIC) == 12:
                break
            else:
                print("Invalid IC. Please enter a valid IC.")

        # Input validation for customer gender
        while True:
            customerGender = input("Gender (M/F) > ")
            if customerGender.upper() == "M" or customerGender.upper() == "F":
                break
            else:
                print("Invalid gender. Please enter M or F.")

        # Input validation for customer date of birth
        while True:
            customerDOB = input("Date of Birth (DD-MM-YYYY) > ")
            try:
                datetime.strptime(customerDOB, '%d-%m-%Y')
                break
            except ValueError:
                print("Invalid format. Please enter a valid date in the format (DD-MM-YYYY).")

        # Input validation for customer email
        while True:
            customerEmail = input("Email > ")
            if "@" in customerEmail and "." in customerEmail.split("@")[-1]:
                break
            else:
                print("Invalid email. Please enter a valid email.")

        # Input validation for customer phone number
        while True:
            customerContactNumber = input("Contact Number > ")
            if customerContactNumber.isdigit() and len(customerContactNumber) == 10:
                break
            else:
                print("Invalid contact number. Please enter a valid number.")

        # Input validation for customer address   
        while True:
            customerAddress = input("Address > ")
            if customerAddress.strip():
                break
            else:
                print("Invalid address. Please enter a valid address.")

        # Input validation for customer account type
        while True:
            customerAccountType = input("Account Type (Savings/Current) > ")
            if customerAccountType.lower() == "savings" or customerAccountType.lower() == "current":
                break
            else:
                print("Invalid account type. Please enter Savings or Current.")

        # Input validation for customer deposit amount
        while True:
            depositAmount = input("Deposit Amount > ")
            if depositAmount.isdigit() and int(depositAmount) > 0:
                break
            else:
                print("Invalid deposit amount. Please enter a positive integer.")

        # create a new list for customer details
        newRecord = [accountNumber,
                     customerPassword,
                     customerName,
                     customerIC,
                     customerGender,
                     customerDOB,
                     customerEmail,
                     customerContactNumber,
                     customerAddress,
                     customerAccountType,
                     depositAmount]

        # save the new record to customer.txt
        customerList.append((customerName, accountNumber))
        with open("customer.txt", "a") as destinationFile:
            newRecordString = ", ".join(newRecord)
            destinationFile.write(newRecordString + "\n")

    # display information for newly created customers
    print("~" * 40)
    print("Customer Information")
    print("~" * 40)
    for customerDetails in customerList:
        print(f"Customer {customerDetails[0]} has the ID {customerDetails[1]}")

    print(f"\n{count} customer accounts have been created successfully\n")


# Function for admin logins
def loginAdmin():
    userList = getDataByColumn("admin.txt")

    print("~" * 40)
    print("Admin Login Page")
    print("~" * 40)

    username = input("Enter Admin username > ")
    password = input("Enter Admin password > ")

    # combine username and password for comparison
    login = username + ", " + password

    # loop through each admin records in text file for valid credentials
    for record in userList:
        loginCredential = record[0] + ", " + record[1]

        # Check if login credentials match 
        if login == loginCredential.strip():
            print("\nLogin Successful\n")
            adminMenu(username)
            return
    else:
        print("\nInvalid username or password. Please try again.\n")


# Function for super user logins
def loginSuperUser():
    userList = getDataByColumn("superuser.txt")

    print("~" * 40)
    print("Super User Login Page")
    print("~" * 40)

    username = input("Enter Super User username > ")
    password = input("Enter Super User password > ")

    # combine username and password for comparison
    login = username + ", " + password

    # loop through each superuser records in text file for valid credentials
    for record in userList:
        loginCredential = record[0] + ", " + record[1]

        # Check if login credentials match         
        if login == loginCredential.strip():
            print("\nLogin Successful\n")
            superUserMenu(username)
            return
    else:
        print("\nInvalid username or password. Please try again.\n")


# function for customer login
def loginCustomer():
    userList = getDataByColumn("customer.txt")

    print("~" * 40)
    print("Customer Login Page")
    print("~" * 40)

    accountNumber = input("Enter account number > ")
    password = input("Enter password > ")

    # combine username and password for comparison
    login = accountNumber + ", " + password

    # loop through each customer records in text file for valid credentials
    for record in userList:
        loginCredential = record[0] + ", " + record[1]

        # Check if login credentials match                 
        if login == loginCredential.strip():
            print("\nLogin Successful\n")
            customerMenu(accountNumber, customerName=record[2])
            return
    else:
        print("\nInvalid username or password. Please try again.\n")


# function to view all admin profiles
def viewAllAdminProfiles():
    # get list of admin users from the file
    userList = getDataByColumn("admin.txt")

    print("~" * 40)
    print("Admin Account List")
    print("~" * 40)

    counter = 1

    # loop through each admin user record and display records   
    for record in userList:
        print(f"{counter}. Admin Username: {record[0]}")
        print(f"Admin Password: {record[1]}\n")
        counter += 1


# function to view all customer profiles
def viewAllCustomerProfiles():
    # get list of customer users from the file
    userList = getDataByColumn("customer.txt")

    print("~" * 40)
    print("Customer Account List")
    print("~" * 40)

    counter = 1

    # loop through each customer user record and display records   
    for record in userList:
        print(f"{counter}. Account Number > {record[0]}")
        print(f"Name > {record[2]}")
        print(f"IC > {record[3]}")
        print(f"Gender > {record[4]}")
        print(f"Date of Birth > {record[5]}")
        print(f"Email > {record[6]}")
        print(f"Contact Number > {record[7]}")
        print(f"Address > {record[8]}")
        print(f"Account Type > {record[9]}")
        print(f"Account Balance > RM{float(record[10]):.2f}\n")
        counter += 1


# function to search customer profiles and details
def searchForCustomerProfile():
    # Get list of customer users from the file
    userList = getDataByColumn("customer.txt")

    print("~" * 40)
    print("Search for Customer Profile")
    print("~" * 40)

    search = input("Enter Customer account number > ")

    # flag to track if the customer profile is found
    found = False

    # loop through each customer user record and display customer details       
    for record in userList:
        if search in record:
            print(f"\nDetails for Customer ID {search}\n")
            print(f"Account Number > {record[0]}")
            print(f"Name > {record[2]}")
            print(f"IC > {record[3]}")
            print(f"Gender > {record[4]}")
            print(f"Date of Birth > {record[5]}")
            print(f"Email > {record[6]}")
            print(f"Contact Number > {record[7]}")
            print(f"Address > {record[8]}")
            print(f"Account Type > {record[9]}")
            print(f"Account Balance > RM{float(record[10]):.2f}\n")

            # set flag to true if the customer profile is found            
            found = True
            break

    if not found:
        print(f"\nAccount Number {search} do not exist.\n")


# function for customer to check balance
def checkBalance(accountNumber):
    # Get list of customer users from the file
    userList = getDataByColumn("customer.txt")

    print("~" * 40)
    print("Account Balance Page")
    print("~" * 40)

    # loop through each customer user record and display customer account balance
    for record in userList:
        if accountNumber == record[0]:
            print(f"Account Balance > RM{float(record[10]):.2f}\n")
            return
    else:
        print("Invalid account number\n")


# function for customer withdrawals
def withdrawal(accountNumber):
    # Get list of customer users from the file
    userList = getDataByColumn("customer.txt")

    print("~" * 40)
    print("Withdrawal Page")

    # loop through each customer user record and find the matching account number
    for index, record in enumerate(userList):
        if accountNumber == str(record[0]):
            # get current account balance and print it
            currentBalance = float(record[10])
            print(f"Current Account Balance > RM{currentBalance:.2f}")
            print("~" * 40)

            while True:
                amount = float(input("Enter withdrawal amount > "))

                # validate that the deposit amount is greater than 0
                if amount > 0:
                    break
                else:
                    print("\nInvalid amount. Please enter a valid amount.\n")

            minimumBalance = getAccountType(accountNumber)
            deposit = float(record[10])

            # check the minimum balance needed for the account type
            if deposit >= minimumBalance and deposit - amount >= minimumBalance:
                updatedBalance = deposit - amount
                record[10] = str(updatedBalance)
                userList[index] = record

                # display successful withdrawal and updated balance 
                print("\nWithdrawal successful\n")
                print(f"New Account Balance > RM{float(record[10]):.2f}\n")

                # save the withdrawal transaction details in the text file
                saveTransaction(record[0], amount, updatedBalance, "Withdrawal")
                saveData("customer.txt", userList)
            else:
                print("\nInsufficient Balance or below minimum balance\n")
            break
    else:
        print("\nInvalid account number\n")


# function for customer deposit
def deposit(accountNumber):
    # Get list of customer users from the file
    userList = getDataByColumn("customer.txt")

    print("~" * 40)
    print("Deposit Page")

    # loop through each customer user record and find the matching account number
    for index, record in enumerate(userList):
        if accountNumber == str(record[0]):
            # get current account balance and print it
            currentBalance = float(record[10])
            print(f"Current Account Balance > RM{currentBalance:.2f}")
            print("~" * 40)

            while True:
                amount = float(input("Enter deposit amount > "))

                # validate that the deposit amount is greater than 0
                if amount > 0:
                    break
                else:
                    print("\nInvalid amount. Please enter a valid amount.\n")

            deposit = float(record[10])
            updatedBalance = deposit + amount
            record[10] = str(updatedBalance)
            userList[index] = record

            # display successful deposit and updated balance 
            print("\nDeposit successful\n")
            print(f"New Account Balance > RM{float(record[10]):.2f}\n")

            # save the deposit transaction details in the text file
            saveTransaction(record[0], amount, updatedBalance, "Deposit")
            saveData("customer.txt", userList)
            break
    else:
        print("\nInvalid account number\n")


# function to print customer's statement of account
def printStatementOfAccount(accountNumber):
    # Get list of transaction from the file
    transactionList = getDataByColumn("transaction.txt")

    startingDate = None
    endingDate = None
    dateRange = None

    print("~" * 40)
    print("Statement of Account Report Generator")
    print("~" * 40)

    # Get start and end dates from user with input validation
    while True:
        startDate = input("Enter start date (YYYY/MM/DD), [B] to go back > ")
        if startDate.lower() == 'b':
            return

        endDate = input("Enter end date (YYYY/MM/DD) > ")
        if endDate.lower() == 'b':
            return

        try:
            startingDate = datetime.strptime(startDate, "%Y/%m/%d")
            endingDate = datetime.strptime(endDate, "%Y/%m/%d")

            if startingDate > endingDate:
                print("\nInvalid date range. Start date should be earlier than end date")
                continue

            dateRange = endingDate - startingDate
        except ValueError:
            print("\nInvalid date format. Please use the format YYYY/MM/DD")
            continue

        break

    # print the statement of account
    print("~" * 40)
    print(f"Statement of Account")
    print(f"Account Number > {accountNumber}")
    print(f"Starting Date > {startDate}")
    print(f"Ending Date > {endDate}")
    print(f"Day Range > {dateRange.days}")
    print("~" * 40)
    print("\nDate", " " * 10, "Description", " " * 10, "Amount", " " * 10, "Account Balance", " " * 10)

    # Loop through each transaction records and print details for the account and date range
    for record in transactionList:
        recordDate = datetime.strptime(record[3], "%Y/%m/%d")

        if record[0] == accountNumber and startingDate <= recordDate <= endingDate:
            transactionType = record[4]
            amount = float(record[1])
            accountBalance = float(record[2])

            print(record[3], " " * 10, transactionType, " " * 15, "RM", amount, " " * 10, "RM", accountBalance,
                  " " * 10)


# function to edit customer password
def editPassword(accountNumber):
    # Get list of customer users from the file
    userList = getDataByColumn("customer.txt")

    # loop through each customer user record and find the matching account number
    for index, record in enumerate(userList):
        if accountNumber == record[0]:
            print(f"\nAccount name > {record[2]}\n")

            # get current password from user 
            currentPassword = input("Enter your current password > ")

            # get new password from user 
            if currentPassword == record[1]:
                newPassword = input("Enter your new password > ")
                confirmPassword = input("Confirm your new password > ")

                # data validation for password
                if newPassword == confirmPassword:
                    # modify the details and write it into the file
                    modifyDetails("customer.txt", 1, userList, record[1], newPassword)
                    print("Password updated successfully.\n")
                else:
                    print("New password do not match.\n")
                return
            else:
                print("Incorrect current password.\n")

    print("Invalid account number\n")


# function to edit customer address
def editCustomerAddress():
    # Get list of customer users from the file
    userList = getDataByColumn("customer.txt")

    accountNumber = input("Enter account number to edit > ")

    # loop through each customer user record and find the matching account number
    for index, record in enumerate(userList):
        if accountNumber == record[0]:
            print(f"\nCustomer Name > {record[2]}")
            print(f"Current address > {record[8]}\n")

            while True:
                # get new address from user
                newAddress = input("Enter new address > ")

                # data validation for address
                if newAddress.strip():
                    # modify the details and write it into the file
                    modifyDetails("customer.txt", 8, userList, record[8], newAddress)
                    print(f"\nNew address > {newAddress}\n")
                    break
                else:
                    print("Invalid address. Please enter a valid address.")
            break
    else:
        print("Invalid account number\n")


# function to edit customer contact number
def editCustomerContactNumber():
    # Get list of customer users from the file
    userList = getDataByColumn("customer.txt")

    accountNumber = input("Enter account number to edit > ")

    # loop through each customer user record and find the matching account number
    for index, record in enumerate(userList):
        if accountNumber == record[0]:
            print(f"\nName > {record[2]}")
            print(f"Current contact number > {record[7]}\n")

            while True:
                # get new contact number from user
                newContactNumber = input("Enter new contact number > ")

                # data validation for new contact number
                if newContactNumber.isdigit() and len(newContactNumber) == 10:
                    # modify the details and write it into the file
                    modifyDetails("customer.txt", 7, userList, record[7], newContactNumber)
                    print(f"\nNew contact number > {newContactNumber}\n")
                    break
                else:
                    print("Invalid contact number. Please enter a valid number.")
            break
    else:
        print("Invalid account number\n")


# function to edit customer email
def editCustomerEmail():
    # Get list of customer users from the file
    userList = getDataByColumn("customer.txt")

    accountNumber = input("Enter account number to edit > ")

    # loop through each customer user record and find the matching account number
    for index, record in enumerate(userList):
        if accountNumber == record[0]:
            print(f"\nName > {record[2]}")
            print(f"Current email > {record[6]}\n")

            while True:
                # get new email from user
                newEmail = input("Enter new email > ")

                # data validation for email
                if "@" in newEmail and "." in newEmail.split("@")[-1]:
                    # modify the details and write it into the file
                    modifyDetails("customer.txt", 6, userList, record[6], newEmail)
                    print(f"\nNew email > {newEmail}\n")
                    break
                else:
                    print("Invalid email format. Please enter a valid email.")
            break
    else:
        print("\nInvalid account number\n")


# function for admin to edit customer details
def modifyCustomerDetails():
    # define current datetime
    currentDateTime = datetime.now()
    currentDate = currentDateTime.strftime("%d/%m/%Y")
    currentTime = currentDateTime.strftime("%H:%M %p")

    while True:
        print("~" * 40)
        print("Modify Customer Details")
        print("Current Date: ", currentDate)
        print("Current Time: ", currentTime)
        print("~" * 40)
        print("\n1. Password")
        print("2. Email")
        print("3. Contact Number")
        print("4. Address")
        print("5. Back\n")
        option = input("Select an option to edit > ")

        if option == "1":
            accountNumber = input("Enter account number to edit password > ")
            editPassword(accountNumber)
        elif option == "2":
            editCustomerEmail()
        elif option == "3":
            editCustomerContactNumber()
        elif option == "4":
            editCustomerAddress()
        elif option == "5":
            print("\nReturning to Admin Page\n")
            break
        else:
            print("\nInvalid option. Please try again\n")


# function for super user main menu
def superUserMenu(username):
    # define current datetime
    currentDateTime = datetime.now()
    currentDate = currentDateTime.strftime("%d/%m/%Y")
    currentTime = currentDateTime.strftime("%H:%M %p")

    while True:
        print("~" * 40)
        print(f"{username}, Welcome to APBank\n")
        print("Current Date: ", currentDate)
        print("Current Time: ", currentTime)
        print("~" * 40)
        print("\n1. Create new admin account")
        print("2. View all admin accounts")
        print("3. Logout\n")
        option = input("Select an option > ")

        if option == "1":
            createAdmin()
        elif option == "2":
            viewAllAdminProfiles()
        elif option == "3":
            print("\nReturning to Login Page\n")
            break
        else:
            print("\nInvalid option. Please try again\n")


# function for admin main menu
def adminMenu(username):
    # define current datetime
    currentDateTime = datetime.now()
    currentDate = currentDateTime.strftime("%d/%m/%Y")
    currentTime = currentDateTime.strftime("%H:%M %p")

    while True:
        print("~" * 40)
        print(f"{username}, Welcome to APBank\n")
        print("Current Date: ", currentDate)
        print("Current Time: ", currentTime)
        print("~" * 40)
        print("\n1. Create new customer account")
        print("2. View all customer account")
        print("3. Search for customer account")
        print("4. Modify customer details")
        print("5. Print Statement of Account")
        print("6. Logout\n")
        option = input("Select an option > ")

        if option == "1":
            createCustomer()
        elif option == "2":
            viewAllCustomerProfiles()
        elif option == "3":
            searchForCustomerProfile()
        elif option == "4":
            modifyCustomerDetails()
        elif option == "5":
            accountNumber = input("Enter account number to print Customer’s Statement of Account Report > ")
            printStatementOfAccount(accountNumber)
        elif option == "6":
            print("\nReturning to Login Page\n")
            break
        else:
            print("\nInvalid option. Please try again\n")


# function for customer main menu
def customerMenu(accountNumber, customerName):
    # define current datetime
    currentDateTime = datetime.now()
    currentDate = currentDateTime.strftime("%d/%m/%Y")
    currentTime = currentDateTime.strftime("%H:%M %p")

    while True:
        print("~" * 40)
        print(f"{customerName}, Welcome to APBank\n")
        print("Current Date: ", currentDate)
        print("Current Time: ", currentTime)
        print("~" * 40)
        print("\n1. Deposit")
        print("2. Withdrawal")
        print("3. Check account balance")
        print("4. Print statement of account")
        print("5. Change password")
        print("6. Logout\n")
        option = input("Select an option > ")

        if option == "1":
            deposit(accountNumber)
        elif option == "2":
            withdrawal(accountNumber)
        elif option == "3":
            checkBalance(accountNumber)
        elif option == "4":
            printStatementOfAccount(accountNumber)
        elif option == "5":
            editPassword(accountNumber)
        elif option == "6":
            print("\nReturning to Login Page\n")
            break
        else:
            print("\nInvalid option. Please try again\n")


# function for the program's main page
def mainMenu():
    # define current datetime
    currentDateTime = datetime.now()
    currentDate = currentDateTime.strftime("%d/%m/%Y")
    currentTime = currentDateTime.strftime("%H:%M %p")

    while True:
        print("~" * 40)
        print("Welcome to APBank")
        print("Current Date: ", currentDate)
        print("Current Time: ", currentTime)
        print("~" * 40)
        print("\n1. Super User Login")
        print("2. Admin Login")
        print("3. Customer Login")
        print("4. Exit\n")
        option = input("Select an option > ")

        if option == "1":
            loginSuperUser()
        elif option == "2":
            loginAdmin()
        elif option == "3":
            loginCustomer()
        elif option == "4":
            print("\nExiting. Thank you for using APBank\n")
            break
        else:
            print("\nInvalid option. Please try again\n")


mainMenu()
