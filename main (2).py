from flask import Flask, render_template, request,redirect
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
    # slug = db.Column(db.String(25), nullable=False, primary_key=True)
    datetime = db.Column(db.String(12), nullable=True)

@app.route('/')
def main():
    return render_template('name.html')


# @app.route('/quiz/<string:quiz_slug>', methods=['GET'])
@app.route('/quiz/<string:sno>', methods=['GET'])
def quiz_route(sno):

    quiz = Quiz.query.filter_by(sno=sno).one()
    return render_template('index.html', quiz=quiz)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if(request.method=='POST'):
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
