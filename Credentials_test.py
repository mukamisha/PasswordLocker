import unittest
from Credentials import Credentials
class TestUserCredentials(unittest.TestCase):
    def setUp(self):
        self.new_user_credentials=Credentials("kevin","kv1",instagram)

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
        objects to our contact_list
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)



if __name__ == '__main__':
    unittest.main()