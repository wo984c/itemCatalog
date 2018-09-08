import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship, backref
from base import Base

from user import EndUser


# Category Model
class Category(Base):

    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    created = Column(DateTime, nullable=False, server_default=func.now())

    modified = Column(DateTime, nullable=False, server_default=func.now(),
                      onupdate=func.current_timestamp())

    uid = Column(Integer, ForeignKey('enduser.id'))
    user = relationship(EndUser, backref='category')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
