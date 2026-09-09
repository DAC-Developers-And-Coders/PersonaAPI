from contextlib import asynccontextmanager
from Routers.arcanas import router as ar
from Routers.personas import router as pr
from Routers.elementos import router as er
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import service

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    service.database.close()

app = FastAPI(
    title="API de Personas",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Allow", "mensagem"]
)

app.include_router(pr)
app.include_router(ar)
app.include_router(er)