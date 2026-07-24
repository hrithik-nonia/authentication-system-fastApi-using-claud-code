from contextlib import asynccontextmanager
from fastapi import FastAPI , Request
from app.database.mongodb import connect_to_mongo, close_mongo_connection
from app.config.settings import settings
from app.exceptions.custom_exception import UserAlreadyExistsException , InvalidCredentialsException
from fastapi.responses import JSONResponse
from app.routes.auth_route import router as auth_router




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


# if user provide existing data during signup
@app.exception_handler(UserAlreadyExistsException)
async def user_already_exists_handler(request: Request, exc: UserAlreadyExistsException):
    return JSONResponse(
        status_code=409,
        content={"detail": exc.message}
    )


# if user provide invalid data during login
@app.exception_handler(InvalidCredentialsException)
async def invalid_credentials_handler(request: Request, exc: InvalidCredentialsException):
    return JSONResponse(
        status_code=401,
        content={"detail": exc.message}
    )


# register routes
app.include_router(auth_router)



@app.get("/")
async def root():
    return {"message": "Auth System API is running 🚀"}

