
from flask import Flask,render_template, request, redirect
from Model import AccountsTable,StudentTable, TeacherTable
from flask_sqlalchemy import SQLAlchemy
from Model.StudentTable import Student
from Model.TeacherTable import Teacher
from Model.AccountsTable import Account
from Model.Database import database
import sqlalchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///MAI.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database.init_app(app)




@app.before_first_request
def create_table():
    database.create_all()

@app.route('/')
def index():
    return render_template('Login/index.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('Login/index.html')

    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']

        account = Account(user, password)
        user_account = database.session.query(Account.username, Account.password).filter_by(username = str(user)).first()

        if user_account is not None:

            if user_account.username == account.username and user_account.password == account.password:
                user_details = database.session.query(Student.first_name,Student.last_name).filter_by(username = str(user_account.username)).first()

                return render_template('Student/Profile.html',firstname = user_details.first_name, lastname = user_details.last_name)



        return render_template('index.html', message= 'Invalid credentials')


@app.route('/RegisterStudent', methods=['GET', 'POST'])
def regStudents():
    if request.method == 'GET':
        return render_template('RegisterStudent.html')

    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        user_check = database.session.query(Student.username).filter_by(username = str(user)).first()
        if user_check is None:
            account = Account(user,password)
            first = request.form['first']
            last = request.form['last']
            id = database.session.query(sqlalchemy.func.max(Student.student_id)).scalar()
            if id is None:
                id = 0
            student = Student(id + 1,user,first,last,None)
            database.session.add(account)
            database.session.add(student)
            database.session.commit()
            return redirect('/')
        else:
            return render_template("RegisterStudentFail.html")


@app.route('/RegisterTeacher', methods=['GET', 'POST'])
def regTeacher():
    if request.method == 'GET':
        return render_template('RegisterTeacher.html')

    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        user_check = database.session.query(Teacher.username).filter_by(username = str(user)).first()
        if user_check is None:
            account = Account(user,password)
            first = request.form['first']
            last = request.form['last']
            id = database.session.query(sqlalchemy.func.max(Teacher.teacher_id)).scalar()
            if id == None:
                id = 0
            teacher = Teacher(id + 1,user,first,last)
            database.session.add(account)
            database.session.add(teacher)
            database.session.commit()
            return redirect('/')
        else:
            return render_template("RegisterStudentFail.html")

@app.route('/datalist')
def RetrieveDataList():
    employees = AccountsTable.Account.query.all()
    return render_template('datalist.html',employees = employees)

@app.route('/StudentList')
def studentData():
    employees = StudentTable.Student.query.all()
    return render_template('StudentList.html', employees=employees)

@app.route('/TeacherList')
def TeacherData():
    employees = TeacherTable.Teacher.query.all()
    return render_template('TeacherList.html', employees=employees)

if __name__ == "__main__":
    app.run(debug=True)