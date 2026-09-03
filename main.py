from fastapi import FastAPI
from controller import router

app = FastAPI(
    title="API de Usuários",
    version="1.0.0"
)

app.include_router(router)
