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
        