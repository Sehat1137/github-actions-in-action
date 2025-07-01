from fastapi import FastAPI

app = FastAPI(title="GitHub Actions in Action")


@app.get("/")
async def root():
    return {"Hello": "World"}
