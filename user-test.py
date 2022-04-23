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
        self.new_user = ('Chris', 'Mwangi', 'kriss')
        
        
        def test_init(self):
            "checking the initialization"
            self.assertEqual(self.new_user.first_name, 'Chris')
            self.assertEqual(self.new_user.last_name, 'Mwangi')
            self.assertEqual(self.new_user.password, 'kriss')
            