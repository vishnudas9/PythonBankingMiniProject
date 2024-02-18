# Mini Banking
# Vishnudas A - D24

_max_allowed_failure = 3
_current_failure_count = 0
_user_data = {}


def create_test_data():
    # user 1
    _user_data_dict = {'username': 'vishnu', 'firstname': 'Vishnudas', 'lastname': 'A', 'dob': '27/10/1992',
                       'mobile': '0123456789', 'accno': '15554587778',
                       'address': 'Thrissur', 'password': '123456', 'aadhar': 123456789012, 'pan': 'ABCDE1234F',
                       'balance': 1000, 'blocked': 0, 'pin': 1234}
    store_user_to_file(_user_data_dict, _user_data_dict['username'])

    # user 2
    _user_data_dict = {'username': 'lakshmi', 'firstname': 'Jyothi', 'lastname': 'Lakshmi', 'dob': '11/11/1996',
                       'mobile': '0123456788', 'accno': '15554587779',
                       'address': 'Thrissur', 'password': '987654', 'aadhar': 123456789013, 'pan': 'ABCDE1234G',
                       'balance': 2000, 'blocked': 0, 'pin': 5634}
    store_user_to_file(_user_data_dict, _user_data_dict['username'])

    # user 3
    _user_data_dict = {'username': 'vihaan', 'firstname': 'Vihaan', 'lastname': 'A', 'dob': '07/05/2021',
                       'mobile': '0123456787', 'accno': '25554587778',
                       'address': 'Thrissur', 'password': '101010', 'aadhar': 123456789014, 'pan': 'ABCDE1234F',
                       'balance': 3000, 'blocked': 0, 'pin': 2468}
    store_user_to_file(_user_data_dict, _user_data_dict['username'])


def clear_screen():
    print("\n" * 5)


def print_welcome_message():
    print("- - - - - - - - - Welcome To- - - - - - - - - - -")
    print("--- - - - - P Y T H O N  B A N K - - - - - - - --")


def print_invalid_input_message():
    print("Invalid Input")


def print_logout_message():
    print("- -  -- You are successfully logged out- -  - - -")
    global _current_failure_count
    global _user_data
    _current_failure_count = 0
    _user_data = {}
    clear_screen()
    print_welcome_message()
    print_login_message()
    user_login()


def print_profile_info():
    global _user_data
    print("- - - - - - - - -My Profile- - - - - - - - - - -")
    print("Name : " + str(_user_data['firstname']) + " " + str(_user_data['lastname']))
    print("Account Number : " + str(_user_data['accno']))
    print("DOB : " + str(_user_data['dob']))
    print("Mobile : " + str(_user_data['mobile']))
    print("Address : " + str(_user_data['address']))
    print("Aadhar Number : " + str(_user_data['aadhar']))
    print("Pan Number : " + str(_user_data['pan']))
    print("- - - - - - - - - - - - - -- - - - - - - - - - -")

    while True:
        goback = input("* Enter E to go back to Main menu : ")
        if goback.upper() == "E":
            clear_screen()
            print_main_menu()
        else:
            print_invalid_input_message()


def check_balance_info():
    global _user_data
    print("- - - -- - - - -Account Info- - - - -- - - - - -")

    print("Account Number : " + str(_user_data['accno']))
    print("Balance : " + str(_user_data['balance']))

    print("- - - - - - - - - - - - - -- - - - - - - - - - -")

    while True:
        goback = input("* Enter E to go back to Main menu : ")
        if goback.upper() == "E":
            clear_screen()
            print_main_menu()
        else:
            print_invalid_input_message()


def withdraw_amount():
    current_bal = float(_user_data['balance'])
    print("- - - -- - - - -Withdraw Cash- - - - -- - - - - -")
    print("Available Balance : " + str(current_bal))

    try:
        while True:
            amount = float(input("Enter Amount to withdraw : "))
            if amount > 0:
                if amount > current_bal:
                    print("Withdrawal amount cannot be higher than available balance!")
                else:
                    while True:
                        pin = str(input("Enter 4 digit transaction security pin : "))
                        if len(pin) == 4 and str(pin) == str(_user_data['pin']):
                            current_bal = current_bal - amount
                            print("Success! New balance amount is : " + str(current_bal))
                            _user_data['balance'] = current_bal
                            update_data(_user_data, _user_data['username'])
                            while True:
                                goback = input("* Enter E to go back to Main menu : ")
                                if goback.upper() == "E":
                                    clear_screen()
                                    print_main_menu()
                                else:
                                    print_invalid_input_message()
                        else:
                            print("Incorrect PIN entered!")
            else:
                print_invalid_input_message()

    except:
        print("Something went wrong! Please try again")
        withdraw_amount()


def deposit_amount():
    current_bal = float(_user_data['balance'])
    print("- - - -- - - - -Deposit Cash- - - - -- - - - - -")
    print("Available Balance : " + str(current_bal))

    try:
        while True:
            amount = float(input("Enter Amount to deposit : "))
            if amount > 0:
                current_bal = current_bal + amount
                print("Success! New balance amount is : " + str(current_bal))
                _user_data['balance'] = current_bal
                update_data(_user_data, _user_data['username'])
                while True:
                    goback = input("* Enter E to go back to Main menu : ")
                    if goback.upper() == "E":
                        clear_screen()
                        print_main_menu()
                    else:
                        print_invalid_input_message()
            else:
                print_invalid_input_message()

    except:
        print("Something went wrong! Please try again")
        deposit_amount()


def transfer_amount():
    current_bal = float(_user_data['balance'])
    print("- - - - - - - - Fund Transfer- - - - - - - - -")
    print("Available Balance : " + str(current_bal))

    try:
        while True:
            amount = float(input("Enter Amount to transfer : "))
            if amount > current_bal:
                print("Transfer amount cannot be higher than available balance!")
            else:
                while True:
                    account_no = int(input("Enter the Beneficiary account number : "))
                    re_account_no = int(input("Re-enter the Beneficiary account number : "))
                    if account_no == re_account_no:
                        while True:
                            ifsc_code = str(input("Beneficiary IFSC Code : "))
                            if len(ifsc_code) >= 6:
                                while True:
                                    pin = str(input("Enter 4 digit transaction security pin : "))
                                    if len(pin) == 4 and str(pin) == str(_user_data['pin']):
                                        current_bal = current_bal - amount
                                        print("Money Transferred! New balance amount is : " + str(current_bal))
                                        _user_data['balance'] = current_bal
                                        update_data(_user_data, _user_data['username'])
                                        while True:
                                            goback = input("* Enter E to go back to Main menu : ")
                                            if goback.upper() == "E":
                                                clear_screen()
                                                print_main_menu()
                                            else:
                                                print_invalid_input_message()
                                    else:
                                        print("Incorrect pin entered!")
                            else:
                                print("Invalid IFSC Code")
                    else:
                        print("Account numbers are not matching! Please try again")
    except:
        print("Something went wrong! Please try again")
        transfer_amount()

def change_pin():
    print("- - - - - - - - Change PIN - - - - - - - - -")
    while True:
        current_pin = input("Enter the current PIN : ")
        if current_pin == str(_user_data['pin']):
            while True:
                new_pin = input("Enter New PIN : ")
                if len(new_pin) == 4:
                    while True:
                        re_new_pin = input("Re-Enter New PIN : ")
                        if new_pin == re_new_pin:
                            print("PIN Changed Successfully!")
                            _user_data['pin'] = new_pin
                            update_data(_user_data, _user_data['username'])
                            while True:
                                goback = input("* Enter E to go back to Main menu : ")
                                if goback.upper() == "E":
                                    clear_screen()
                                    print_main_menu()
                                else:
                                    print_invalid_input_message()
                        else:
                            print("Re-entered PIN Numbers are not matching. Please try again.")
                else:
                    print("PIN number should be in 4 digits")
        else:
            print("Incorrect PIN!")


def change_password():
    print("- - - - - - - - Change Password- - - - - - - - -")
    while True:
        current_password = input("Enter the current Password : ")
        if current_password == str(_user_data['password']):
            while True:
                new_password = input("Enter New Password : ")
                if len(new_password) >= 6:
                    while True:
                        re_new_password = input("Re-Enter New Password : ")
                        if new_password == re_new_password:
                            print("Password Changed Successfully!")
                            _user_data['password'] = new_password
                            update_data(_user_data, _user_data['username'])
                            while True:
                                goback = input("* Enter E to go back to Main menu : ")
                                if goback.upper() == "E":
                                    clear_screen()
                                    print_main_menu()
                                else:
                                    print_invalid_input_message()
                        else:
                            print("Re-entered Password are not matching. Please try again.")
                else:
                    print("Password number should be greater than 6 digits")
        else:
            print("Incorrect Password!")


def print_main_menu():
    print("- - - - - - - - - Main Menu- - - - - - - - - - -")
    print("1. Balance Check")
    print("2. Withdraw Fund")
    print("3. Transfer Fund")
    print("4. Deposit Fund")
    print("5. My Profile")
    print("6. Change PIN")
    print("7. Change Password")
    print("8. Logout")
    print("- - - - - - - - - - - - - -- - - - - - - - - - -")
    option = int(input("Enter your choice to continue:"))

    # process logout
    if option == 1:
        check_balance_info()
    elif option == 2:
        withdraw_amount()
    elif option == 3:
        transfer_amount()
    elif option == 4:
        deposit_amount()
    elif option == 5:
        print_profile_info()
    elif option == 6:
        change_pin()
    elif option == 7:
        change_password()
    elif option == 8:
        print_logout_message()


def print_user_greeting(_username):
    print("Hello! " + _username)


def print_success_login_msg(_loginname):
    print("Welcome back! " + _loginname)


def print_user_notfound_msg():
    print("Invalid username. Please try again")


def print_incorrect_password_msg():
    print("Incorrect Password! Please try again")
    global _current_failure_count
    _current_failure_count += 1
    print_login_message()
    user_login()


def print_login_message():
    print("\nPlease Login To Continue:")


def print_maxlimit_warning():
    print("\nMax login attempt reached. Kindly try after sometime:")


def user_login():
    if _current_failure_count < 3:
        _username = input("Username: ")
        _password = input("Password: ")
        _user_info = load_users_from_file(_username)

        if _user_info:
            if _password == _user_info['password']:
                print_success_login_msg(str(_user_info['firstname']))
                global _user_data
                _user_data = _user_info.copy()
                print_main_menu()
            else:
                print_incorrect_password_msg()
    else:
        print_maxlimit_warning()


def update_data(dictionary, username):
    try:
        with open(username + '.txt', 'w') as file:
            for key, value in dictionary.items():
                file.write(f'{key}: {value}\n')
        file.close()
    except Exception as e:
        print("Something went wrong!")

def store_user_to_file(dictionary, username):
    try:
        with open(username + '.txt', 'w') as file:
            for key, value in dictionary.items():
                file.write(f'{key}: {value}\n')
        print("Dictionary data written to file successfully.")
        file.close()
    except Exception as e:
        print(f"Error writing dictionary data to file: {e}")


def load_users_from_file(username):
    try:
        with open(username + '.txt', 'r') as file:
            lines = file.readlines()
            my_dict = {}
            for line in lines:
                key, value = line.strip().split(':')
                my_dict[key.strip()] = value.strip()
            file.close()
            return my_dict
    except FileNotFoundError:
        print("User not found.")
        print_login_message()
        user_login()
    except Exception as e:
        print(f"Error reading dictionary data from file: {e}")


# CODE EXECUTION BEGINS HERE
create_test_data()
print_welcome_message()
print_login_message()
user_login()
