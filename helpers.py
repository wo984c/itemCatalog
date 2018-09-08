from flask import Flask, redirect, render_template
from flask import session as login_session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base
from models.user import EndUser

import os

from functools import wraps


NOT_AUTH_ERR = "<script>function myFunction() " \
               + "{alert('You are not authorized.');" \
               + "window.location.href = '/';}" \
               + "</script><body onload='myFunction()''>"


def init_app():

    app = Flask(__name__)
    app.secret_key = 'super_secret_key'

    return app

app = init_app()


def init_db():
	# Data Base connection
    engine = create_engine(
        'postgresql://itemcatalog:uD@c1ty185!@localhost/itemcatalog')

    Base.metadata.bind = engine

    # Data Base session
    DBSession = sessionmaker(bind=engine)

    return DBSession()

session = init_db()


# Login Required Decorator
def login_required(f):
    @wraps(f)
    def x(*args, **kwargs):
        if 'username' not in login_session:
            return redirect('/login')

        return f(*args, **kwargs)

    return x


# Customization of 404 and 500 errors
@app.errorhandler(500)
def server_err(e):
    return render_template('exceptions.html',
                           err="500 - Internal Server Error"), 500


@app.errorhandler(404)
def page_not_found(e):
    return render_template('exceptions.html', err="404 - Page not found"), 404


def createUser(login_session):
    newUser = EndUser(name=login_session['username'], email=login_session[
                   'email'])
    session.add(newUser)
    session.commit()
    user = session.query(EndUser).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(EndUser).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(EndUser).filter_by(email=email).one()
        return user.id
    except:
        return None
