#!/usr/bin/env python3.6
from Credentials import Credentials

def create_account(account_user_name,password):
        '''
        Function to create a new account
        '''
        new_account = Credentials(account_user_name,password)
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
        short-code = input().upper()
        if short_code == 'CR'
                print("New account")
                print("-"*10)

                print("Enter your UserName:")
                u_name=input()

                print("Enter your password")
                p_wrd=input()

                # print("Enter your accountName")
                # ac_name=input()

                # save_account(create_account(u_name,p_wrd,ac_name))


