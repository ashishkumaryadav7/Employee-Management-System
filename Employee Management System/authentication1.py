class authentication:
    def __init__(self,username,password):
        self.username=username
        self.password=password

    # function that verify the username and password if correct then return True else False
    def verifcation(self):
        if(self.username=="ashish" and self.password=="123"):
            return True
        else:
            return False





