from flask import Flask, render_template, request,jsonify, json, session, redirect

from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import basedir

import Main, cfg
from IO import inputFormat


app = Flask(__name__)

app.secret_key = 'qwerty1'

app.config.from_object('config')
db = SQLAlchemy(app)

import models
lm = LoginManager()
lm.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods = ['POST'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    if _name and _email and _password:
        if(checkEmailName(_name, _email)):
            addRecord(_name,_email, _password)
            return json.dumps({'html': '<span>All fields good !!</span>'})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

    _hashed_password = generate_password_hash(_password)


def addRecord(_name,_email, _password):
    u = models.User(name=_name, password=_password, email=_email)
    db.session.add(u)
    db.session.commit()

def checkEmailName(name, email):
    users = models.User.query.all()
    for u in users:
        if (u.email == email or u.name == name):
            return False
    return True
@app.route('/showLogIn')
def showSignin():
    return render_template('login.html')

@app.route('/validateLogin', methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']


        if (checkUserPassword(_username, _password)):
            session['user'] = _username + _password
            return redirect('/userHome')
        else:
            return render_template('error.html', error='Wrong Email address or Password.')


    except Exception as e:
        return render_template('error.html', error=str(e))



def checkUserPassword(username, password):
    users = models.User.query.all()
    for u in users:
        if (u.email == username):
            if(u.password == password):
                return True
    return False

@app.route('/userHome')
def userHome():
    print(session.get('user'))
    if(session.get('user')):
        return render_template('userHome.html')
    else:
        return render_template('error.html', error='Unauthorized access')


@app.route('/userHome/data', methods=['GET', 'POST'])
def getData():
    try:
        Main.main(inputFormat.format(json.loads(request.data)))
        return json.dumps((123)), 200, {'ContentType': 'application/json'}
    except Exception as e:
        return render_template('error.html', error=e)

@app.route('/result', methods=['GET', 'POST'])
def result():
    try:
        if (session.get('user')):
            return render_template('result.html',
                               CNTNR_SS=cfg.CNTNR_SS,
                               CNTNR_C = cfg.CNTNR_C,
                               CNTNR_IR = cfg.CNTNR_IR)
        else:
            return render_template('error.html', error='Unauthorized access')

    except Exception as e:
        return render_template('empty.html')

    finally:
        cfg.CNTNR_SS = None
        cfg.CNTNR_C = None
        cfg.CNTNR_IR = None

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/guide')
def guide():
    return render_template('guide.html')


if __name__ == '__main__':
    app.run()
