from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

router = APIRouter()

class CitizenIn(BaseModel):
    national_id: str
    first_name: str
    last_name: str

class CitizenOut(CitizenIn):
    id: str

# In-memory store for stubs (replace with DB in next steps)
_DB: dict[str, dict] = {}

@router.get("/", response_model=List[CitizenOut])
async def list_citizens():
    return list(_DB.values())

@router.get("/{citizen_id}", response_model=CitizenOut)
async def get_citizen(citizen_id: str):
    doc = _DB.get(citizen_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Citizen not found")
    return doc

@router.post("/", response_model=CitizenOut, status_code=201)
async def create_citizen(payload: CitizenIn):
    # very simple stub implementation
    new_id = str(uuid.uuid4())
    doc = {"id": new_id, "national_id": payload.national_id, "first_name": payload.first_name, "last_name": payload.last_name}
    _DB[new_id] = doc
    return doc
