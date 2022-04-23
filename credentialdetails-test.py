import unittest
from credentialdetails import credential

class TestCredentials(unittest.TestCase):
    """
    Class helping to create testcases for creds
    """
    
    def setUp(self):
        
        """
        runs before testcases are run
        """
        self.new_credential = credential('instagram','kriss-cream','beddes')
        
        
    def tearDown(self):
        """
        cleanup after testcases are run
        """
        credential.cred_list = []
        
    def test_init(self):
        """
        checks that initialization is successful
        """
        self.assertEqual(self.new_credential.account_name,'instagram')
        self.assertEqual(self.new_credential.username, 'kriss-cream')
        self.assertEqual(self.new_credential.password, 'beddes')
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()


 