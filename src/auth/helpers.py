import hashlib
import uuid
from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import schemas
from . import models


def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + password.encode()).hexdigest()

def get_users(db: Session):
    return db.query(models.User).all()

def create_new_user(db: Session, user: schemas.CreateUser):
    if user.password != user.password_confirm:
        raise HTTPException(status_code=400, detail='Passwords do not match!')
    password = hash_password(user.password)
    db_user = models.User(email=user.email, is_active=user.is_active, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db_profile = models.Profile(user_id=db_user.id)
    db.add(db_profile)
    db.commit()
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()