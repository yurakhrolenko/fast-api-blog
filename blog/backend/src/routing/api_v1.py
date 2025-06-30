from fastapi import APIRouter

from .article import router as article_router

api_routes = [
    article_router,
]

api_router = APIRouter()

for route in api_routes:
    api_router.include_router(route)

__all__ = ['api_router']
