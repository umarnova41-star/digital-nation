from fastapi import APIRouter, Header
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class MeOut(BaseModel):
    sub: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None

@router.get("/me", response_model=MeOut)
async def me(authorization: Optional[str] = Header(None)):
    """
    Stub /me endpoint. In production this will validate the JWT (Keycloak).
    For now it returns token header-ish info if Authorization header present.
    """
    if not authorization:
        return MeOut()  # anonymous
    # naive parse for demo (DO NOT use in production)
    token = authorization.split(" ", 1)[-1]
    return MeOut(sub="stub-sub", username="stub-user", email="stub@example.org")
