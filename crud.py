from sqlalchemy.orm import Session
from models import User, Blog
import bcrypt


def get_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, username: str, password: str):
    hashed_password = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
    user = User(username=username, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def check_username_password(
    db: Session, username: str, password: str, check_existency: bool
):
    if check_existency:
        user = get_by_username(db, username)
        if user is None:
            return {"msg": "User does not exist."}
    return bcrypt.checkpw(password.encode("utf8"), user.password)


def create_blog(db: Session, user_id: int, title: str, content: str):
    blog = Blog(user_id=user_id, title=title, content=content)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def get_blogs(db: Session, user_id: int):
    return db.query(Blog).filter(Blog.user_id == user_id).all()


def get_blog_by_id(db: Session, blog_id: int):
    return db.query(Blog).filter(Blog.id == blog_id).first()
