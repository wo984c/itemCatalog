# Connects to the PostgreSQL database called itemcatalog using the username
# itemcatalog and creates the schema.

from models.base import *
from models.user import *
from models.item import *
from models.category import *

from sqlalchemy import create_engine


engine = create_engine(
    'postgresql://itemcatalog:uD@c1ty185!@localhost/itemcatalog')

Base.metadata.create_all(engine)
