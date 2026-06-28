from fastapi import FastAPI

from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:changeme@localhost/fullstack"

engine = create_engine(DATABASE_URL, echo=True)
connection = engine.connect()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

