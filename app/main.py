from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database.mongodb import connect_to_mongo, close_mongo_connection
from app.config.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    yield
    # Shutdown
    await close_mongo_connection()


app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {"message": "Auth System API is running 🚀"}