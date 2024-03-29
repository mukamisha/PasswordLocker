import unittest
from Credentials import Credentials
class TestUserCredentials(unittest.TestCase):
    def setUp(self):
        self.new_user_credentials=Credentials("kevin","kv1","instagram")

    def test_init(self):
        """
        to test if an object is initialised properly
        """
        self.assertEqual(self.new_user_credentials.account_user_name,"kevin")
        self.assertEqual(self.new_user_credentials.password,"kv1")
        self.assertEqual(self.new_user_credentials.accountName,"instagram")


    def test_save_user_credentials(self):
        '''
        this is to  test  if the user object is saved into
        the credential list
        '''

        self.new_user_credentials.save_user_credentials() # saving the new details intered
        self.assertEqual(len(Credentials.credentials_list),1)


    def test_save_multiple_user_credentials(self):
        '''
        to check if we can save multiple user dredentials in our credential list

        '''
        self.new_user_credentials.save_user_credentials()
        test_new_credentials = Credentials("evelyn","ev3","linkedin") # new credential
        test_new_credentials.save_user_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def tearDown(self):
            '''
            for cleaning up after each test case .
            '''
            Credentials.credentials_list = []  
            
    def test_delete_user_credentials(self):
            '''
            for deleting user accounts or credentials in need.
            '''
            self.new_user_credentials.save_user_credentials()
            test_new_credentials = Credentials("umuhire","hu2","facebook",) # new credential
            test_new_credentials.save_user_credentials()
            self.new_user_credentials.delete_user_credentials()# Deleting a credential object
            self.assertEqual(len(Credentials.credentials_list),1)

    def test_display_all_user_Credentials(self):
        '''
        this will return the list of all credentials we have
        '''

        self.assertEqual(Credentials.display_user_credentials(),Credentials.credentials_list)

    # def test_check_user_credentials(self):
    #     '''
    #     Function to test whether the login in function check_user works as expected
    #     '''
    #     self.new_user_credentials = Credentials("kke","kevi345","kv&gmail.com")
    #     self.new_user_credentials.save_user_credentials()
    #     new_user = Credentials("hey","hi23","kv&gmail.com")
    #     new_user.save_user_credentials()
    #     for user in Credentials.credentials_list:
    #         if user.account_user_name == new_user.account_user_name and user.password == new_user.password:
    #             current_user = user.account_user_name
    #     return current_user
    #     self.assertEqual(current_user,Credentials.check_user_credentials(new_user.password,new_user.user_name))

    

    

if __name__ == '__main__':
    unittest.main()