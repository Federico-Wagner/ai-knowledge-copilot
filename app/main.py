from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Knowledge Copilot")

app.include_router(router)