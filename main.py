from fastapi import FastAPI
from controller import router
from Model.Database import Database as Db

banco_de_dados = Db()

app = FastAPI(
    title="API de Personas",
    version="1.0.0"
)

app.include_router(router)