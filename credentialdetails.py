import string
import random

class credential:
    """
    Generates new instances of user credential details
    
    """
    cred_list = []
    
    def __init__(self,account_name,username,password):
        """
        oobject properties defined
        Args:
            account_name:new account name
            username:new username
            password:new password
        """
        self.account_name = account_name
        self.username = username
        self.password = password
    
    
    def save_creds(self):
        """
        saving credential information to the cred_list
        """
        
        self.cred_list.append(self)
        
        
    @classmethod
    def display_creds(cls):
        """
        retuns creds list
        """
        return cls.cred_list
        
        
        
    
        
    
    