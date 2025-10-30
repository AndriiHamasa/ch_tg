from fastapi import FastAPI
from app.db.database import engine, Base
from app.routers import channel_router

# Base.metadata.create_all(bind=engine)

app = FastAPI(title="CMS-LLM APP API", version="1.0.0")

app.include_router(channel_router)

@app.get("/")
async def root():
    return {"message": "Hello, Andrii)"}
