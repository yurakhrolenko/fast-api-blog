from typing import List
from fastapi import APIRouter, Depends

from src.schemas.article import ArticleSchema
from src.services.article import ArticleService
from src.depends import get_article_service

router = APIRouter(
    prefix='/articles',
    tags=['Пости'],
)


@router.get(
   "",
   responses={400: {"description": "Bad request"}},
   response_model=List[ArticleSchema],
   description="Отримання всіх постів",
)
async def get_all_books(
       article_service: ArticleService = Depends(get_article_service),
) -> List[ArticleSchema]:
   books = article_service.get_articles()
   return books
