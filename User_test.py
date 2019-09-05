import unittest
from User import User
class TestUserDetails(unittest.TestCase):
    def setUp(self):
        self.new_user_details=User("sasa","dada")

    def test_init(self):
        """
        to test if an object is initialised properly
        """
        self.assertEqual(self.new_user_details.account_user_name,"sasa")
        self.assertEqual(self.new_user_details.password,"dada")

    def test_save_user_details(self):
        '''
        this is to  test  if the user object is saved into
        the user list
        '''

        self.new_user_details.save_user_details() # saving the new details intered
        self.assertEqual(len(User.user_list),1)
  


if __name__ == '__main__':
    unittest.main()
