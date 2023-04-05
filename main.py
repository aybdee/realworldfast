from fastapi import FastAPI
from routes import user
from dotenv import load_dotenv
app = FastAPI()


@app.get("/ok")
def healthcheck():
    pass


app.include_router(user.router, prefix="/api/user", tags=["user"])
