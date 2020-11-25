from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/quizzania_db'
db = SQLAlchemy(app)
class Questions(db.Model):
    # sno, email, phone, msg, datetime
    sno = db.Column(db.Integer(), primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    opt1 = db.Column(db.String(100),  nullable=False)
    otp2 = db.Column(db.String(100),  nullable=False)
    otp3 = db.Column(db.String(100), nullable=False)
    otp4 = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.String(12), nullable=False)
@app.route('/')
def contacts():
    # name = "Bhashkar Bhatt"
    return render_template('index.html')
app.run()









# db.session.add(User(name="Flask", email="example@example.com"))
# db.session.commit()

# users = User.query.all()
# @app.route('/contacts'), methods=['GET', 'POST']
# def contacts():
#     if(request.method=="POST"):
#         # add entry to the database
#         name=request.form.get('name')



# from flask import Flask, session, redirect, url_for, request
# from markupsafe import escape
#
# app = Flask(__name__)
#
# # Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#
# @app.route('/')
# def index():
#     if 'username' in session:
#         return 'Logged in as %s' % escape(session['username'])
#     return 'You are not logged in'
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#         <form method="post">
#             <p><input type=text name=username>
#             <p><input type=submit value=Login>
#         </form>
#     '''
#
# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))
