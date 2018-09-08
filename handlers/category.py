from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session

from sqlalchemy import asc, desc
from sqlalchemy.exc import IntegrityError

import string
import os

from models.category import *
from models.item import *
from helpers import *


# Show Categories and recently added items on the main page
@app.route('/')
@app.route('/catalog/')
def listCategories():

    categories = session.query(Category).order_by(
        asc(Category.name)).all()

    recentItems = session.query(Item).order_by(
        desc(Item.modified)).limit(10).all()

    if 'username' not in login_session:

        return render_template('public_categories.html',
                               categories=categories, recentItems=recentItems)

    else:

        return render_template('categories.html', categories=categories,
                               recentItems=recentItems,
                               usr=login_session['username'])


# Add Category
@app.route('/catalog/newcategory/', methods=['GET', 'POST'])
@login_required
def newCategory():

    if request.method == 'POST':

        try:

            new = Category(name=request.form['name'],
                           uid=login_session['user_id'])

            session.add(new)
            session.commit()

            flash("Category %s has been created" % new.name)

        except IntegrityError:

            session.rollback()
            flash("Category %s not created. Looks like it already exists."
                  % new.name)

        return redirect(url_for('listCategories'))

    else:

        return render_template('newcategory.html',
                               usr=login_session['username'])


# Delete Category
@app.route('/catalog/<string:category_name>/delete/', methods=['GET', 'POST'])
@login_required
def delCategory(category_name):

    cat2del = session.query(Category).filter_by(name=category_name).one()

    if cat2del.uid != login_session['user_id']:

        return NOT_AUTH_ERR

    if request.method == 'POST':

        session.delete(cat2del)
        session.commit()
        flash("Category %s has been deleted" % cat2del.name)
        return redirect(url_for('listCategories'))

    else:

        return render_template('delcategory.html', category=cat2del,
                               usr=login_session['username'])


# Edit Category
@app.route('/catalog/<string:category_name>/edit/', methods=['GET', 'POST'])
@login_required
def editCategory(category_name):

    cat2edit = session.query(Category).filter_by(name=category_name).one()

    if cat2edit.uid != login_session['user_id']:

        return NOT_AUTH_ERR

    if request.method == 'POST' and request.form['name']:

        cat2edit.name = request.form['name']
        session.add(cat2edit)
        session.commit()
        flash("Category %s has been modified"
              % (category_name))

        return redirect(url_for('listCategories'))

    else:

        return render_template('editcategory.html', category=cat2edit,
                               usr=login_session['username'])
