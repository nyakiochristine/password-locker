import unittest
from user import User
from credentialdetails import Credential
import random
import string


def register_user(f_name,l_name, u_name, password):
    """
    new user registration
    """
    new_user = User(f_name,l_name,u_name,password)
    new_user.save_user()
    
    
def login_user():
    """
    Logs in the user
    """
    username = input("Enter your username \n")
    password = input("Enter your password \n")
    
    
    if User.user_exists(username):
        for user in User.user_list:
            if user.username == username and password==password:
                return True
            else:
                print("Username or password is incorrect. Please try again.")
                
    else:
        print("Username or password is does not exist. Please.")
        anykey = input("Enter your password and username")
        return False
    
    def make_credentials(account_name,username, password):
        """
        make new credentials

        """
        save_credentials(Credential(account_name,username,password))
        
        
    def save_credentials(creds):
        """
        stores credentials in the database
        """
        Credential.cred_list.append(creds)
        
        
    ef display_credentials():
        """
        method to display credentials
        """

        
        
        
       
        

def main():
        """
        runs before other functions
        """
        while True:
            selector = input("Welcome to this password manager! Type in the following")
            
        





if __name__ == '__main__':
    main()

