from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.secret_key = 'balaji766'
db = SQLAlchemy(app)


class User(db.Model):
    email = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String)
    password = db.Column(db.String, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    due_date = db.Column(db.Date)
    status = db.Column(db.String)

    user_id = db.Column(db.String, db.ForeignKey('user.email'))
    user = relationship("User", backref="tasks")

    def __init__(self, title, description, due_date, status, user):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.user = user


@app.route('/')
def homePage():
    return render_template('registerPage.html')


@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('pswd')

    user = User.query.filter_by(email=email).first()
    if user:
        return "User already exists!"

    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return "Signed up successfully!"


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('pswd')

    user = User.query.filter_by(email=email, password=password).first()
    if user:
        session['email'] = email
        return render_template('homePage.html', name=user.name)
    else:
        return 'User not found!'


@app.route('/createTask.html')
def createTaskRoute():
    return render_template('createTask.html')


@app.route('/createTask', methods=['POST'])
def createTask():
    email = session['email']
    title = request.form.get('title')
    description = request.form.get('description')
    due_date = datetime.strptime(request.form['due-date'], '%Y-%m-%d').date()
    status = request.form.get('status')

    user = User.query.filter_by(email=email).first()
    new_task = Task(title=title, description=description, due_date=due_date, status=status, user=user)
    db.session.add(new_task)
    db.session.commit()

    return 'Task created successfully!'


@app.route('/listAllTasks.html')
def listAllTasks():
    email = session['email']
    user = User.query.filter_by(email=email).first()
    tasks = Task.query.filter_by(user=user).all()
    return render_template('listAllTasks.html', tasks=tasks)


@app.route('/retrieveTask.html')
def retrieveTaskroute():
    return render_template('retrieveTask.html')


@app.route('/retrieveTask', methods=['POST'])
def retrieveTask():
    task_id = request.form.get('task_id')
    email = session['email']
    user = User.query.filter_by(email=email).first()
    task = Task.query.filter_by(id=task_id, user=user).first()

    if task:
        return render_template('retrieveTask.html', task=task)
    else:
        return 'Task not found'


@app.route('/updateTask.html')
def updateTaskRoute():
    email = session['email']
    user = User.query.filter_by(email=email).first()
    tasks = Task.query.filter_by(user=user).all()
    return render_template('updateTask.html', tasks=tasks)


@app.route('/updateTask', methods=['POST'])
def updateTask():
    task_id = request.form.get('task_id')
    title = request.form.get('title')
    description = request.form.get('description')
    due_date = datetime.strptime(request.form['due-date'], '%Y-%m-%d').date()
    status = request.form.get('status')

    task = Task.query.get(task_id)
    if task:
        task.title = title
        task.description = description
        task.due_date = due_date
        task.status = status
        db.session.commit()
        return 'Task updated successfully!'
    else:
        return 'Task not found'


@app.route('/deleteTask.html')
def deleteTaskroute():
    return render_template('deleteTask.html')


@app.route('/deleteTask', methods=['POST'])
def deleteTask():
    task_id = request.form.get('task_id')
    email = session['email']
    user = User.query.filter_by(email=email).first()
    
    task = Task.query.filter_by(id=task_id, user=user).first()

    if task:
        db.session.delete(task)
        db.session.commit()
        message = "Task with ID {} has been deleted.".format(task_id)
    else:
        message = "Task with ID {} does not exist or you do not have permission to delete it.".format(task_id)

    return render_template('deleteTask.html', message=message)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
