import string
import random


class Credential:
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
    
    def delete_creds(self):
        """
        delets saved credentials if no longer needed by user
        """
        credential.cred_list.remove(self)
        
        
    @classmethod
    def generate_password(cls,username):
        """
        to generate random passcodes
        """
        randomSource = string.ascii_letters + string.digits + string.punctuation
        password +=random.choose(string.ascii_lowercase)
        password += random.choose(string.ascii_uppercase)
        password += random.choose(string.digits)
        password += random.choose(string.punctuation)
        
        for i in range (6):
            password += random.choice(randomSource)
        listPassword =list(password)
        random.SystemRandom().shuffle(listPassword)
        password = ''.join(listPassword)
        return password
    
    
            
        
    
        
        
        
        
    
        
    
    