from pydantic import BaseModel


class ArticleSchema(BaseModel):
    id: int
    title: str
    content: str
    author_id: int | None
