from fastapi import APIRouter
from pydantic import BaseModel, Field

# routers
router = APIRouter()

@router.get("/user")
async def read_user():
    return "user"

# db models
from db import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)