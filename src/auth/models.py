from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from ..settings import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    profile = relationship('Profile', uselist=False, back_populates='user', cascade="all, delete")


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='profile')

    name = Column(String(30), default='')
    surname = Column(String(30), default='')
    avatar_url = Column(String, default='')  