from typing import List

from src.schemas.article import ArticleSchema


class ArticleRepository:
    __ARTICLES = [
        {
            'id': 1,
            'title': 'article 1',
            'content': 'article 1 content',
            'author_id': None,
        },
        {
            'id': 2,
            'title': 'article 2',
            'content': 'article 2 content',
            'author_id': None,
        },
    ]

    def get_articles(self) -> List[ArticleSchema]:
        return [ArticleSchema(**item) for item in self.__ARTICLES]

    def create_article(self) -> ArticleSchema:
        ...
