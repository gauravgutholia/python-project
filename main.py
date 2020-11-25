from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/quizzania_db'
db = SQLAlchemy(app)
class Quiz(db.Model):
    # sno, question, opt1, otp2, opt3, opt4, datetime
    sno = db.Column(db.Integer(), primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    opt1 = db.Column(db.String(100),  nullable=False)
    opt2 = db.Column(db.String(100),  nullable=False)
    opt3 = db.Column(db.String(100), nullable=False)
    opt4 = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.String(12), nullable=True)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    if(request.method=='POST'):
        # Add entry to the DataBase
        question = request.form.get('question')
        opt1 = request.form.get('opt1')
        opt2 = request.form.get('opt2')
        opt3 = request.form.get('opt3')
        opt4 = request.form.get('opt4')
        entry = Quiz(question = question, opt1 = opt1, opt2 = opt2, opt3 = opt3, opt4 = opt4, datetime=datetime.now())
        db.session.add(entry)
        db.session.commit()
   
   
    return render_template('backend.html')
app.run(debug=True)







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
