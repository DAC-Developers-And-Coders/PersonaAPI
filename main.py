from contextlib import asynccontextmanager
from Routers.arcanas import router as ar
from Routers.personas import router as pr
from Routers.elementos import router as er
from fastapi import FastAPI
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

app.include_router(pr)
app.include_router(ar)
app.include_router(er)