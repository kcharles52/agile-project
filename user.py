class User:
    users =[]

    def __init__(self,username,password):
        """Initialise class instances """
        self.username = username
        self.password = password

    def signup(self):
        User.users.append(self)
        return True
