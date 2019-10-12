from user import User
import getpass
from file_account import FileAccount


class CliInterface:

    def __init__(self):
        self.user = User()

    def main_menu(self):
        print("====Crypto pass application====")
        print("1. Connection")
        print("2. Create an account")
        print("3. Help")
        print("================================")

        valid_option = False
        options = ['1', '2', '3']
        option = None
        while not valid_option:
            option = input("Please enter the option chosen:")
            if option in options:
                valid_option = True
            else:
                print("The option given is not valid. Please try again")

        if option == '1':
            self.__account_connection()
        if option == '2':
            self.__account_creation()
        if option == '3':
            print("help to give")

    def __account_creation(self):
        print("====Account creation====")
        print("please enter a username that will be used to connect to the application")
        username = input("Enter a username:")
        valid = False
        while not valid:
            password = getpass.getpass(prompt="Enter a password: ")
            rep_password = getpass.getpass(prompt="Enter a password: ")
            if password != rep_password and password is not None:
                print("Passwords given differ from each other. Please try again.")
            else:
                valid = True

        self.user.new_account(username, password)

    def __account_connection(self):
        print("====Account Connection====")
        print("Welcome to you on the Crypto pass application.")
        print("to Login please enter your information.")

        connected = False
        while not connected:
            username = input("Enter your username:")
            password = input("Enter your password:")

            connected = self.user.existing_account(username, password)

            if not connected:
                print("Impossible to decrypt information. Data are probably incorrect. Try again")
            else:
                print("You are now connected.")
                connected = True

    def manage_menu(self):
        print("Welcome to your management space dear ", self.user.get_username())
        file_account = FileAccount(self.user.get_cipher(), self.user.get_filename())
        while True:
            print("Menu")
            file_account.display_all_accounts()
            break
