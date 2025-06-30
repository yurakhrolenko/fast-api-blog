from typing import List

from src.repositories.article import ArticleRepository
from src.schemas.article import ArticleSchema


class ArticleService:

    def __init__(self, repository: ArticleRepository) -> None:
        self.repository = repository

    def get_articles(self) -> List[ArticleSchema]:
        result = self.repository.get_articles()
        return result

    def create_article(self) -> ArticleSchema:
        result = self.repository.create_article()
        return result