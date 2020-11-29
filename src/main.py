from fastapi import FastAPI
from .auth.routers import router

app = FastAPI()

app.include_router(router, prefix='/users')