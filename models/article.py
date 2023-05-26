from db.base_class import Base
import sqlalchemy as db
from sqlalchemy.orm import relationship
from models.user import User
from sqlalchemy.ext.mutable import MutableList



class Article(Base):
    __tablename__ = "article"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(500))
    slug = db.Column(db.String(500),unique=True)
    description = db.Column(db.String(500))
    favorites_count = db.Column(db.Integer,default=0)
    body = db.Column(db.String(10000))
    tagList = db.Column(MutableList.as_mutable(db.PickleType),default=[])
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    author = relationship("User")


    
    

    
    

    
