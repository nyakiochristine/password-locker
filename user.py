class User:
    
    """
    class  generating new instance for user
    """
    user_list = []
    
    
    def __init__(self,first_name,last_name, username,password):
     """
     Obj Properties
     
      Args:
            first_name: New user first name.
            last_name: New user last name.
            username: New user username.
            password: New user password.
     """"
     self.first_name = first_name
     self.last_name = last_name
     self.username = username
     self.password = password
     
     
     def save_user(self):
         """"
         Saves objects to the list of users
         """
         self.user_list.append(self)
         
         
         @classmethod
         def user_exists(cls,logged_user):
             """
             Checks if user exists

             Args:
                 logged_user: username of logged user used to search for user
                 return: True if user exists
             """
             for user in cls.user_list:
                 if user.username ==logged_user:
                     return True
                 return False
                 
                     

     
     