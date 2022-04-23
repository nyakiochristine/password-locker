import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    defines tests for user
    


    """
    
    def setUp(self):
        """
        method running before tests are run
        """
        self.new_user = ('Chris', 'Mwangi','cream-ks', 'kriss')
        
        
        def test_init(self):
            """
            method used to check if the initialization is successful
            """
            self.assertEqual(self.new_user.first_name, 'Chris')
            self.assertEqual(self.new_user.last_name, 'Mwangi')
            self.assertEqual(self.new_user.username, 'cream-ks')
            self.assertEqual(self.new_user.password, 'kriss')
            
        def test_save_user(self):
            """
            check if the user info is saved
            """
            self.new_user.save_user = ()
            self.assertEqual(len(User.user_list),1)
            
        def test_user_exists(self):
            """
            checking if information abt users exists
            """
            self.new_user.save_user()
            self.assertTrue(User.user_exists('cream-ks'))

if __name__ == '__main__':
    unittest.main()

