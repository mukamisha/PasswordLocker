class Credentials:
    """
    this class creates a new instance of a class user
    """
    credential_list=[]

    
    def __init__(self,account_user_name,password,):

        self.account_user_name = account_user_name
        self.password = password
       

    def save_user_details(self):
        '''
        save_user_details method saves user objects into 
        user_list
        '''
        Credentials.credential_list.append(self)