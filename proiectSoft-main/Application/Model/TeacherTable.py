from Model.Database import database

class Teacher(database.Model):
    __tablename__ = "Teacher"

    teacher_id = database.Column(database.Integer, primary_key= True)

    user = database.Column(database.String, database.ForeignKey('Account.username'))
    username = database.Column(database.String, database.ForeignKey('Account.username'))
    first_name = database.Column(database.String, nullable= False)
    last_name = database.Column(database.String, nullable=False)



    def __init__(self, student_id, username, first_name, last_name):
        self.student_id = student_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return self.student_id +":" + self.username +":" + self.first_name +":" + self.last_name

    def __repr__(self):
        return self.student_id +":" + self.username +":" + self.first_name +":" + self.last_name
