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
     
     