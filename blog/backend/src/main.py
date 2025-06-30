from fastapi import FastAPI

from .routing.api_v1 import api_router

app = FastAPI(
    title="Blog API",
    version="1.0.0",
    responses={404: {'description': 'Not found'}},
)

app.include_router(api_router)
