import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship, backref
from base import Base

from category import Category
from user import EndUser


# Item Model
class Item(Base):

    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    description = Column(String(250))
    created = Column(DateTime, nullable=False, server_default=func.now())

    modified = Column(DateTime, nullable=False, server_default=func.now(),
                      onupdate=func.current_timestamp())

    catid = Column(Integer, ForeignKey('category.id'))

    category = relationship(Category, backref=backref('item',
                            cascade='all, delete'))

    uid = Column(Integer, ForeignKey('enduser.id'))
    user = relationship(EndUser, backref='item')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
