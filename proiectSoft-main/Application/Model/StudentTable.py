from Model.Database import database

class Student(database.Model):
    __tablename__ = "Student"

    student_id = database.Column(database.Integer, primary_key= True)

    username = database.Column(database.String,database.ForeignKey('Account.username'))
    first_name = database.Column(database.String, nullable= False)
    last_name = database.Column(database.String, nullable=False)
    year = database.Column(database.Integer,nullable=True)



    def __init__(self, student_id, username, first_name, last_name, year):
        self.student_id = student_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.year = year

    def __str__(self):
        return self.student_id +":" + self.username +":" + self.first_name +":" + self.last_name +":" + self.year

    def __repr__(self):
        return self.student_id +":" + self.username +":" + self.first_name +":" + self.last_name +":" + self.year
