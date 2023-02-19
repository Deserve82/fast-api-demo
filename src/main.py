from fastapi import FastAPI, Depends

from src.infra.database import engine
from src.domain import gecko, user
from src.api import gecko_router

gecko.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(gecko_router.router)


@app.get("/")
def health_checker():
    return "gecko is healthy!"
