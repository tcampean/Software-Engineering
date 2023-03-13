from Model.Database import database

class Account(database.Model):
    __tablename__ = "Account"

    username = database.Column(database.String, primary_key= True)
    password = database.Column(database.String, nullable= False)


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username +":" + self.password

    def __repr__(self):
        return self.username + ":" + self.password
