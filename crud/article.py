from sqlalchemy.orm import Session
from models.article import Article
from schemas import article as article_schema
from random import randint as ri


def find_by_slug(slug:str,db:Session):
    return db.query(Article).filter(Article.slug == slug).first()

def generate_slug(title:str,db:Session):
    def generate_sub():
        for i in range(3):
            return ''.join([chr(ri(97,122)) for i in range(4)])
    
    title = title.split(" ")
    title_slice = title[ri(0,len(title))]
    slug = f"{title_slice}{generate_sub()}"
    if find_by_slug(slug,db):
        slug = generate_slug(title,db)
    return slug
    
    


def create_article(article:article_schema.Article,db:Session):
    article.slug = generate_slug(article.title,db)
    new_article = Article(**article.dict())
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def delete_article(slug:str,db:Session):
    db.query(Article.slug == slug).delete()
