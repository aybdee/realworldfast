from pydantic import BaseModel
from typing import List, Optional


class Article(BaseModel):
    title:str
    author_id:Optional[int]
    slug:Optional[str]
    description:str
    body:str
    tagList:Optional[List[str]]
    
  

class ArticleEdit(BaseModel):
    title:Optional[str]
    description:Optional[str]
    body:Optional[str]

class ArticleEditWrapped(BaseModel):
    article:Article

    
class ArticleWrapped(BaseModel):
    article:Article

   
class ArticleDisp(Article):
    pass

