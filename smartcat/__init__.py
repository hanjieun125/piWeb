import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartcat.db' #'mysql://root:''@localhost/crud'
app.config['SQlALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

<<<<<<< HEAD
class LangAlarmConf(db.Model):
    __tablename__ = 'tblLangAlarmConf'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alarmtime = db.Column(db.DateTime(timezone=True),default=datetime.datetime.now)
    def __intit__(self, alarmtime):
        self.alarmtime = alarmtime

=======
>>>>>>> f8b68647842be49d0d50ae21c42dca9c85362dca
class LangAlarmWord(db.Model):
    __tablename__ = 'tblLangAlarmWord'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(30), unique=False, nullable=True)
    word = db.Column(db.String(100), unique=False, nullable=False)
    memo = db.Column(db.String(200), unique=False, nullable=True)
    cntplayed = db.Column(db.Integer, unique=False, nullable=True)
    useyn = db.Column(db.String(1), unique=False, nullable=True)
    regdate = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)

    def __init__(self, category, word, memo):
        self.category = category
        self.word = word
        self.memo = memo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pages/<page>')
def pages(page):
    return render_template('/pages/'+page)
    
@app.route('/contents/<page>')
def contents(page):
    return render_template('/contents/'+page)

<<<<<<< HEAD
@app.route('/bbs/list.html')
def bbslist():
    read_data = LangAlarmWord.query.all()
    return render_template('/bbs/list.html',langwords = read_data)

@app.route('/bbs/add.html')
def bbslistadd():
    read_data = LangAlarmWord.query.all()
    return render_template('/bbs/add.html',langwords = read_data)   

@app.route('/bbs_save_add', methods=['POST'])
=======
@app.route('/bbs/<page>')
def bbs(page):
    all_data = LangAlarmWord.query.order_by(LangAlarmWord.id.desc()).all()
    return render_template('/bbs/'+page, langwords = all_data)

@app.route('/bbs_insert', methods=['POST'])
>>>>>>> f8b68647842be49d0d50ae21c42dca9c85362dca
def bbsinsert():
    category = request.form['category']
    word = request.form['word']
    memo = request.form['memo']
    newWord = LangAlarmWord(category,word,memo)
    db.session.add(newWord)
    db.session.commit()
<<<<<<< HEAD
    return "add success"
=======
    return "success"
>>>>>>> f8b68647842be49d0d50ae21c42dca9c85362dca
