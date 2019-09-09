#!/usr/bin/env python3.6
from Credentials import Credentials
from User import User

def create_account(user_name,password):
        '''
        Function to create a new account
        '''
        new_account = User(user_name,password)
        return new_account

def save_user_detail(user):
        '''
        Function to save a new user account
        '''
        user.save_user_details()

def verify_user(user_name,password):
        '''
        Function that verifies the existance of the user before creating credentials
        '''
        checking_user = Credentials.check_user(user_name,password)
        return checking_user

def create_credentials_account(account_user_name,password,account_name):
        '''
        Function to create a credential account
        '''
        new_credential_account = Credentials(account_user_name,password,account_name)
        return new_credential_account


def generate_password():
	'''
	Function to generate a password for the user
	'''
	paswrd_g = Credentials.generate_password()
	return paswrd_g

def save_user_credentials(credentials):
        '''
        Function to save contact
        '''
        credentials.save_user_credentials()


def del_user_credentials(credentials):
        '''
        Function to delete a credential
        '''
        credentials.delete_user_credentials()


        
def display_user_credentials():
        '''
        Function that returns all the saved credentials
        '''
        return Credentials.display_user_credentials()
def main():
        print("Hello!!  Welcome to our PasswordLock App. What is your name?")
        user_name=input()

        print(f"Hi {user_name}. what do you want to do?")
        print('\n')

        while True:

                    print("use the following short codes : CR - creating a new account,LG - to login, EXI - to exit")
                    short_code = input().upper()
                    
                    if short_code == "EXI":
                        print("bye .......")
                        break

                    elif short_code == 'CR':
                        print("New account")
                        print("-"*20)

                        print("Enter your UserName:")
                        user_name=input()

                        print("Enter your password")
                        pass_word=input()

                        # print("Enter your accountName")
                        # ac_name=input()

                        save_user_detail(create_account(user_name,pass_word))
                        print('\n')
                        print(f"A new account {user_name} {pass_word} has been successfully created")
                        print('\n')

                    elif short_code =='LG':
                        print("-"*20)
                        print('')
                        print("Enter your account details to login")
                        print('\n')
                        
                        user_name = input("enter your username:")
                        password = input("enter your password:")
                        user_exists = verify_user(user_name,password)
                        if user_exists == user_name:
                                print("\n")
                                print("please use those shortcodes to continue: ")
                                
                                print("-"*30)
                                print("enter: AD - to create credential , DS - to display credential , DL - to delete crdential,EX - to exit the application ")
                                short_code = input().upper()

                                if short_code == 'EX':
                                        print("bye....")
                                        break

                                elif short_code == 'AD':
                                        print('\n')
                                        print("enter your credential account details:")
                                        account_user_name = input("enter your account user name:")
                                        account_name = input("enter your account name:") 
                                        
                                        print('\n')
                                        print("select password option: AP - for the app to generate it for you , SEL - for yourself to generate it ")

                                        short_code = input().upper()
                                        print("-"*50)

                                        if short_code == 'AP':
                                                print('\n')
                                                password = generate_password()
                                                # break
                                        elif short_code == 'SEL':
                                                print('\n')
                                                password = input("enter your password:")
                                                


                                        else :
                                                print("invalid input")

                                        save_user_credentials(create_credentials_account(account_user_name,password,account_name))
                                        print('\n')
                                        print(f"credential account :{account_user_name} ,{password},{account_name} has been successfully created")
                                        print('\n')

                                elif short_code == 'DS':
                                        if display_user_credentials():
                                                print("here is your credentials's list:")
                                                print('\n')

                                                for cred in display_user_credentials():
                                                        print(f"{account_user_name} ,{password},{account_name}")
                                                        print('\n')
                                                
                                        else:
                                                        print('\n')
                                                        print("you don't seem to have any credential yet, please create one")

                        else:
                                print("invalid input!!")


if __name__ == '__main__':
    main()

