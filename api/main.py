from fastapi import FastAPI

app = FastAPI(title="GitHub Actions in Action")


@app.get("/", description="Root endpoint")
async def root():
    return {"Hello": "World"}
