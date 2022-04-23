import unittest
from credentialdetails import Credential

class TestCredentials(unittest.TestCase):
    """
    Class helping to create testcases for creds
    """
    
    def setUp(self):
        
        """
        runs before testcases are run
        """
        self.new_credential = Credential('instagram','kriss-cream','beddes')
        
        
    def tearDown(self):
        """
        cleanup after testcases are run
        """
        Credential.cred_list = []
        
    def test_init(self):
        """
        checks that initialization is successful
        """
        self.assertEqual(self.new_credential.account_name,'instagram')
        self.assertEqual(self.new_credential.username, 'kriss-cream')
        self.assertEqual(self.new_credential.password, 'beddes')
        
    def test_save_creds(self):
        """
        check if its possible to save info in the cred_list
        """
        self.new_credential.save_creds()
        self.assertEqual(len(Credential.cred_list),1)
        
        
    def test_save_multiple_creds(self):
        """
        check if its possible to save many cred objects on the list
        
        """
        self.new_credential.save_creds()
        test_credential = Credential('pinterest','kennie','labr')
        test_credential.save_creds()
        self.assertEqual(len(Credential.cred_list),2)
        
    def test_display_creds(self):
        """
        test if credential details can be displayed
        """
        self.assertEqual(Credential.display_creds(), Credential.cred_list )
        
    def test_delete_creds(self):
        """
        test case to check if one can remove creds that one does not need
        """
        self.new_credential.save_creds()
        test_credential= Credential('pinterest','kennie','labr')
        test_credential.delete_creds
        
        
        self.assertEqual(len(Credential.cred_list),1)
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()


 