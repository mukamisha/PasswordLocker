class User:
    """
    this class creates a new instance of a class user
    """
    user_list=[]


    def __init__(self,user_name,password):

        self.user_name = user_name
        self.password = password
        

    def save_user_details(self):
        '''
        save_user_details method saves user objects into 
        user_list
        '''
        User.user_list.append(self)

