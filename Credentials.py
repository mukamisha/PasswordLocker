from User import User
import random
import string

class Credentials:
    """
    this class creates a new instance of a class user
    """
    credentials_list=[]

    
    def __init__(self,account_user_name,password,accountName):

        self.account_user_name = account_user_name
        self.password = password
        self.accountName=accountName
       

    def save_user_credentials(self):
        '''
        save_user_details method saves user objects into 
        user_list
        '''
        Credentials.credentials_list.append(self)

    def delete_user_credentials(self):
        '''
        deletes a user credentials in a credential list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_user_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credentials_list


    def generate_password(size=5,char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Function to generate a password for the user
        '''
        paswrd_g=''.join(random.choice(char) for _ in range(size))
        return paswrd_g

    @classmethod
    def check_user(cls,user_name,password):
        '''
        Method that checks if the name and password entered match entries in the users_list
        '''
        current_user = ''
        for x in User.user_list:
            if (x.user_name == user_name and x.password == password):
                current_user = x.user_name
        return current_user