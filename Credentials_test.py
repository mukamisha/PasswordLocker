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
        objects to our credentials_list
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
            
    def test_delete_contact(self):
            '''
            for deleting user accounts or credentials in need.
            '''
            self.new_user_credentials.save_user_credentials()
            test_new_credentials = Credentials("umuhire","hu2","facebook",) # new credential
            test_new_credentials.save_user_credentials()
            self.new_user_credentials.delete_user_credentials()# Deleting a credential object
            self.assertEqual(len(Credentials.credentials_list),1)

    

if __name__ == '__main__':
    unittest.main()