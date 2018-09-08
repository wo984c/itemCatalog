import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship, backref
from base import Base


# User model
class EndUser(Base):

    __tablename__ = 'enduser'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=False)
    email = Column(String(250), nullable=False)
    created = Column(DateTime, nullable=False, server_default=func.now())
    modified = Column(DateTime, nullable=False, server_default=func.now(),
                	  onupdate=func.current_timestamp())
