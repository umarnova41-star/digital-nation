from fastapi import FastAPI
from app.api.v1.routers import auth, citizens
from app.core.config import settings

app = FastAPI(title="Digital Nation Platform API", version="0.1.0")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(citizens.router, prefix="/api/v1/citizens", tags=["citizens"])

@app.get("/health")
async def health():
    return {"status": "ok"}
