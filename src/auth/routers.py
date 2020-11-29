from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import schemas
from .helpers import create_new_user, get_user_by_id, get_users
from ..settings import SessionLocal


router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/', response_model=schemas.User, status_code=201)
def register(user: schemas.CreateUser, db: Session = Depends(get_db)):
    new_user = create_new_user(db, user)
    return new_user

@router.get('/', response_model=List[schemas.User])
def get_users_list(db: Session = Depends(get_db)):
    users_list = get_users(db)
    return users_list

@router.get('/{user_id}', response_model=schemas.UserDetail)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User does not exist')
    return user

@router.delete('/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User does not exist')
    db.delete(user)
    db.commit()
    return ''