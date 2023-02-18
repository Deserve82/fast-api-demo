from fastapi import FastAPI

from src.infra.database import engine
from src.domain import gecko, user

gecko.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def health_check():
    return "gecko is running"
