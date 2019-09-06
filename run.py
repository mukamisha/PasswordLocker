#!/usr/bin/env python3.6
from Credentials import Credentials
from User import User

def create_account(account_user_name,password):
        '''
        Function to create a new account
        '''
        new_account = Credentials(account_user_name,password)
        return new_account

def save_user_details(user):
        '''
        Function to save a new user account
        '''
        User.save_user_details()

def verify_user(user_name,password):
        '''
        Function that verifies the existance of the user before creating credentials
        '''
        checking_user = Credentials.check_user_credentials(user_name,password)
        return checking_user

def create_credentials_account(account_user_name,password,account_name):
        '''
        Function to create a credential account
        '''
        new_credential_account = Credentials(account_user_name,password,account_name)
        return new_account

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

                    print("use the following short codes : CR - creating a new account,LN - to log_in, EXI - to exit")
                    short-code = input().upper()
                    if short-code =='EXI':
                        break
                    

                    elif short_code == 'CR':
                        print("New account")
                        print("-"*20)

                        print("Enter your UserName:")
                        u_name=input()

                        print("Enter your password")
                        p_wrd=input()

                        print("Enter your accountName")
                        ac_name=input()

                        save_user(create_user(u_name,p_wrd,ac_name))
                        print('\n')
                        print(f"A new account {u_name} {p_wrd} {ac_name} has been successfully created")
                        print('\n')

                    elif short_code =='LN':
                        print("-"*20)
                        print('')
                        print("To be able to login enter your account details:")
                        print('\n')
                        user_name = input("enter your userName")
                        passWord = input("enter your password")
                        user_exists = verify(user_name,password)
                        if user_exists == user_name:
                            print(f"welcome {user_name}. please choose another option to proceed")
                            print("\n")

                            while True:
                                        print("use those short codes: CC - create credential account, DC - display user_credentials,DL - to delete a credential ")
                                        short_code = input().upper()
                                        if short_code == 'CC':
                                                print("new credential account")
                                                print("-"*20)

                                                print("enter user_name:")
                                                user_N = input()

                                                print("enter account_name: ")
                                                acc = input()

                                                print("enter password")
                                                pass_word = input()


                                                save_credentials(create_credentials_account(account_user_name,password,account_name))
                                                print('\n')
                                                print(f"new credential account {account_user_name},{password},{account_name} has been successfully created")
                                                print('\n')





if __name__ == '__main__':
    main()

