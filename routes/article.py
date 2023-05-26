from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from models.article import Article
from schemas.article import ArticleEditWrapped, ArticleWrapped
from db.session import get_db
from crud import article as article_crud
from schemas.user import User
from utils.auth import get_current_user_oauth
from utils.exceptions import ArticleError, ArticleException


router = APIRouter()



@router.post("/")
def create_article(article: ArticleWrapped, db:Session= Depends(get_db),current_user=Depends(get_current_user_oauth)):
    article.article.author_id  = current_user.id
    article = article_crud.create_article(article.article,db) 
    return {"article":article}


@router.put("/{slug}")
def update_article( slug:str,article_update:ArticleEditWrapped, db:Session=Depends(get_db),current_user=Depends(get_current_user_oauth)):
    article = article_crud.find_by_slug(slug,db)
    if article:
        if article.author_id == current_user.id:
            properties = [
                "title",
                "description",
                "body"
            ]
            for property in properties:
                if getattr(article_update.article,property):
                    setattr(article,property,getattr(article_update.article,property))
            
            db.commit()
            db.refresh(article)
            
            return {"article":article}
        else:
            return ArticleException(ArticleError.NotAllowedToEdit)
    else:
        return ArticleException(ArticleError.ArticleNotExist)


@router.delete("/{slug}") 
def delete_article(slug:str,db:Session= Depends(get_db), current_user= Depends(get_current_user_oauth)):
    article = article_crud.find_by_slug(slug,db)
    if article:
        if article.author_id == current_user.id:
            article_crud.delete_article(slug,db)
        else:
            return ArticleException(ArticleError.NotAllowedToEdit)
    else:
        return ArticleException(ArticleError.ArticleNotExist)


 
