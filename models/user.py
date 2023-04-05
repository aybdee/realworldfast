from db.base_class import Base
from sqlalchemy.orm import relationship
import sqlalchemy as db


class User(Base):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True)
    token = db.Column(db.String(20), unique=True, nullable=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    bio = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String(50), nullable=True)
    following_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    following = relationship('User', remote_side=[id])
