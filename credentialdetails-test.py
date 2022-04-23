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
        self.new_cred = credential('instagram','kriss-cream','beddes')
        

 