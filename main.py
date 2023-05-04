from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from routes import user
from dotenv import load_dotenv
import requests
app = FastAPI()


@app.get("/ok")
def healthcheck():
    pass


app.include_router(user.router, prefix="/api/user", tags=["user"])
