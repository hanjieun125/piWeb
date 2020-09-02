<<<<<<< HEAD
#-*- coding: utf-8 -*-
from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shindalsoo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
=======
# -*- coding: utf-8 -*-
from gtts import gTTS
from playsound import playsound
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hanjieun.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://id@비밀번호'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
>>>>>>> d8b2d830b0d485e921adebe1783698e47dfdd1e1

db = SQLAlchemy(app)

class Employee(db.Model):
<<<<<<< HEAD
    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    tel = db.Column(db.String(50))
    position = db.Column(db.String(50))    

    def __init__(self, username, email, tel,position):
=======
    userid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    tel = db.Column(db.String(50))
    position = db.Column(db.String(50))

    def __init__(self, username, email,tel,position):
>>>>>>> d8b2d830b0d485e921adebe1783698e47dfdd1e1
        self.username = username
        self.email = email
        self.tel = tel
        self.position = position

@app.route('/')
def index():
    all_data = Employee.query.order_by(Employee.userid.desc()).all() # select * from employee
<<<<<<< HEAD
    return render_template("index.html", employees=all_data)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
=======
    #return 'hello flask'
    return render_template("index.html", employees = all_data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
>>>>>>> d8b2d830b0d485e921adebe1783698e47dfdd1e1
        username = request.form['username']
        email = request.form['email']
        tel = request.form['tel']
        position = request.form['position']

<<<<<<< HEAD
        insertUser = Employee(username,email,tel,position)
=======
        insertUser = Employee(username, email, tel,position)
>>>>>>> d8b2d830b0d485e921adebe1783698e47dfdd1e1
        db.session.add(insertUser)
        db.session.commit()

        return redirect(url_for('index'))

@app.route('/delete/<uid>')
def delete(uid):
<<<<<<< HEAD
    delUser = Employee.query.get(uid) # select * from Employee where userid=3
=======
    delUser = Employee.query.get(uid) #select * from Employee where userid = 3 
>>>>>>> d8b2d830b0d485e921adebe1783698e47dfdd1e1
    db.session.delete(delUser)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        updateUser = Employee.query.get(request.form.get('userid'))
<<<<<<< HEAD
        updateUser.username = request.form['username']
=======
        updateUser.username =  request.form['username']
>>>>>>> d8b2d830b0d485e921adebe1783698e47dfdd1e1
        updateUser.email = request.form['email']
        updateUser.tel = request.form['tel']
        updateUser.position = request.form['position']
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search():
    txtsearch = request.form['txtsearch']
    searchUser = Employee.query.filter(Employee.username.contains(txtsearch))
    return render_template("index.html", employees=searchUser, txtsearch=txtsearch)

@app.route('/playmp3')
def playmp3():
<<<<<<< HEAD
    text = "오늘은, 2020년 8월 20일입니다. 고양이가 소리를 내려고합니다. 우리모두 스마트고양이를 응원합시다~~람쥐"
    filename = "hellosmartcat.mp3"
    tts = gTTS(text=text, lang='ko')
    tts.save(filename)
    playsound(filename)

=======
    text = "오늘은, 2020년 8월 20일 입니다. 고양이가 소리를 내려고합니다. 우리모두 스마트고양이를 응원합시다~~람쥐"
    filename = "hello smartcat.mp3"
    tts = gTTS(text=text, lang='ko')
    tts.save(filename)
    playsound(filename)   
>>>>>>> d8b2d830b0d485e921adebe1783698e47dfdd1e1
    return "고양이가 소리를 냈습니다."