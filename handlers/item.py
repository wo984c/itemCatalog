from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session

from sqlalchemy import asc, desc
from sqlalchemy.exc import IntegrityError

import string
import os

from models.category import *
from models.item import *
from helpers import *


# Show Items for specific category
@app.route('/catalog/<string:category_name>/')
def listItems(category_name):

    category = session.query(Category).filter_by(name=category_name).one()
    allItems = session.query(Item).filter_by(catid=category.id).all()

    if 'username' not in login_session:

        return render_template('public_items.html', category=category,
                               items=allItems)

    else:

        return render_template('items.html', category=category, items=allItems,
                               usr=login_session['username'])


# Show item's description
@app.route('/catalog/<string:category_name>/<string:item_name>/')
def describeItem(category_name, item_name):

    item = session.query(Item).filter_by(name=item_name).one()
    category = session.query(Category).filter_by(name=category_name).one()

    if 'username' not in login_session:

        return render_template('public_idescript.html', item=item,
                               category=category)

    else:

        return render_template('itemdescript.html', item=item,
                               category=category,
                               usr=login_session['username'])


# Add Item
@app.route('/catalog/<string:category_name>/items/new/',
           methods=['GET', 'POST'])
@login_required
def addItem(category_name):

    catname = session.query(Category).filter_by(name=category_name).one()

    if catname.uid != login_session['user_id']:

        return NOT_AUTH_ERR

    if request.method == 'POST':

        try:

            new = Item(name=request.form['name'], description=request.form[
                'description'], catid=catname.id, uid=login_session['user_id'])
            session.add(new)
            session.commit()
            flash("Item %s has been created." % new.name)

        except IntegrityError:

            session.rollback()
            flash("Item %s not created. Looks like it already exists."
                  % new.name)

        return redirect(url_for('listItems', category_name=category_name))

    else:

        return render_template('additem.html', category=catname,
                               usr=login_session['username'])


# Edit Item
@app.route('/catalog/<string:category_name>/<string:item_name>/edit/',
           methods=['GET', 'POST'])
@login_required
def editItem(category_name, item_name):

    item2edit = session.query(Item).filter_by(name=item_name).one()
    category = session.query(Category).filter_by(name=category_name).one()

    if item2edit.uid != login_session['user_id']:

        return NOT_AUTH_ERR

    if request.method == 'POST' and request.form['description']:

        item2edit.name = request.form['name']
        item2edit.catid = request.form['category']
        item2edit.description = request.form['description']

        session.add(item2edit)
        session.commit()

        flash("Item %s has been modified"
              % (item2edit.name))

        return redirect(url_for('listItems', category_name=category_name))

    else:

        cats = session.query(Category).filter_by(
                uid=login_session['user_id']).all()

        return render_template('edititem.html', cats=cats, category=category,
                               item=item2edit, usr=login_session['username'])


# Delete Item
@app.route('/catalog/<string:category_name>/<string:item_name>/delete/',
           methods=['GET', 'POST'])
@login_required
def delItem(category_name, item_name):

    item2del = session.query(Item).filter_by(name=item_name).one()
    category = session.query(Category).filter_by(name=category_name).one()

    if item2del.uid != login_session['user_id']:

        return NOT_AUTH_ERR

    if request.method == 'POST':

        session.delete(item2del)
        session.commit()
        flash("Item %s has been deleted" % item2del.name)
        return redirect(url_for('listItems', category_name=category_name))

    else:

        return render_template('delitem.html', category=category,
                               item=item2del, usr=login_session['username'])
