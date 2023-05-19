from db.base_class import Base
from sqlalchemy.orm import relationship
import sqlalchemy as db
from db.session import get_db

class User(Base):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    token = db.Column(db.String(300), unique=True, nullable=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    bio = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String(100), nullable=True)
    following_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    following = relationship("User")#, remote_side=[id])



   
# session = next(get_db())
#
# olduser = session.query(User).filter(User.username == "sweet").first()
# olduser2 = session.query(User).filter(User.username == "notsweet").first()
#
# newuser = User(email="reallysweet@gmail.com",username="reallysweet",password="password",following=[olduser,olduser2])
#
# session.add(newuser)
# session.commit()

