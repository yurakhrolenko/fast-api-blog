from src.repositories.article import ArticleRepository
from src.services.article import  ArticleService

"""
Файл внедрения зависимостей
"""
# repository - работа с БД
article_repository = ArticleRepository()

# service - слой UseCase
article_service = ArticleService(article_repository)


def get_article_service() -> ArticleService:
   return article_service