from fastapi import FastAPI

from controllers import LoginController, UrlsController

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(LoginController.router)
app.include_router(UrlsController.router)
