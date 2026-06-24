from fastapi import FastAPI
from backend.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)


@app.get("/")
def root():
    return {"message": "ResearchForge API is running 🚀"}


@app.get("/health")
def health_check():
    return {"status": "ok"}