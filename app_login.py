from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:'..postgresql password..'@localhost/login'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MOSIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'Feedback'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(200))

    def __init__(self, username, password):

        self.username = username
        self.password = password



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2.html/')
def index2():
    return render_template('index2.html')

@app.route('/success.html/')
def success():
    return render_template('success.html')



@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['pass']
        #print( user, password)
    
    

        if user == '':
            return render_template('index.html', message='Please enter required fields')
        
        if db.session.query(Feedback).filter(Feedback.username == user).count() == 0:
            data = Feedback( user, password)
            db.session.add(data)
            db.session.commit()
            #send_mail(customer, dealer, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted feedback')
    


if __name__ == '__main__':

    app.run()
