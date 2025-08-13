from sqlalchemy.orm import Session
from . import models, utils

def create_user(db: Session, username: str, password: str):
    hashed_password = utils.hash_password(password)
    user = models.User(username=username, password_hash=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()
