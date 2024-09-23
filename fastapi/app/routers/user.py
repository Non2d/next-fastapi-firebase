from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field

router = APIRouter()

@router.get("/user")
async def read_user():
    return "user"