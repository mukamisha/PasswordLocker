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

    @classmethod
    def check_user_credentials(cls,account_user_name,password):
        '''
        Method that checks if the name and password entered match entries in the users_list
        '''
        current_user_credentials = ''
        for user in Credentials.credentials_list:
            if (user.account_user_name == account_user_name and user.password == password):
                current_user_credentials = user.user_name
        return current_user_credentials