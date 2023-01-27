import os
from typing import Union
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn

load_dotenv()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, item: Union[str, None] = None):
    return {"item_id": item_id, "q": item}


def main():
    uvicorn.run(app, host="localhost", port=int(int(os.getenv("PORT") or 8000)))


if __name__ == "__main__":
    main()
