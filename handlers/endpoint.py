from flask import jsonify
from models.item import Item
from models.category import Category
from helpers import *
import string
import json
import os


# Returns JSON with the entire catalog
@app.route('/catalog/json/')
def catalogJSON():

    categories = session.query(Category).all()
    cDict = [c.serialize for c in categories]
    cDictLen = len(cDict)

    for c in range(cDictLen):

        items = [i.serialize for i in session.query(Item).filter_by(
            catid=cDict[c]["id"]).all()]

        if items:

            cDict[c]["item"] = items

    return jsonify(Category=cDict)


# Returns JSON with Catalog's Categories
@app.route('/catalog/categories/json/')
def categoriesJASON():

    categories = session.query(Category).all()
    return jsonify(categories=[c.serialize for c in categories])


# Returns JSON with items for a given category
@app.route('/catalog/<string:category_name>/items/json/')
def categoryItemJSON(category_name):

    category = session.query(Category).filter_by(name=category_name).one()
    catitems = session.query(Item).filter_by(catid=category.id).all()
    return jsonify(items=[i.serialize for i in catitems])


# Returns JSON with an specific item
@app.route('/catalog/<string:category_name>/<string:item_name>/json/')
def itemJSON(category_name, item_name):

    category = session.query(Category).filter_by(name=category_name).one()
    item = session.query(Item).filter_by(name=item_name,
                                         catid=category.id).one()
    return jsonify(item=[item.serialize])
