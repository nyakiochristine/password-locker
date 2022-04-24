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
        
        
    def display_credentials():
        """
        method to display credentials
        """
        return Credential.cred_list
    
    
    def generate_password(username):
        """
        random passcode
        """
        return Credential.generate_password(username)
    
    
    def delete_credentials(creds):
        """
        function to delete credentials
        """
        return Credential.delete_credentials(creds)
    
    
    
    
    
        

        
        
        
       
        

def main():
        """
        runs before other functions
        """
        while True:
            print("\033c")
            selector = input("Welcome to this password manager! Type in the following:\n \n \"log\"- to login to your account \n to \"register\"- to register \n \"exit\"- to exit from application \n \n ")
            print("."*14)
            
            
            if selector =="register":
                print("\033c")
                f_name =input("Enter your first name \n")
                l_name =input("Enter your last name \n")
                u_name =input("Enter your username \n")
                password =input("Enter your password \n")
                register_user(f_name,l_name,u_name,password)
                print("\n")
                print("Account registered successfully!")
                anykey= input("Press any key to proceed...")
                continue
            
            elif selector =="login":
                print("\033c")
                logged_in = login_user()
                
                while logged_in:
                    print("\033c")
                    print(" Welcome back to this password manager.Type the following: \n ne-to create a new credential details,\n save-to save new credential details, \n display-to display all credential details,\n quit-to leave this section")
                
                
                             
         
         
            
            
            
            
            
        





if __name__ == '__main__':
    main()

