from fastapi import APIRouter

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
    uid = Column(String(255), index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)

class TestProduct(Base):
    __tablename__ = "test_products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(255), index=True)
    price = Column(Integer, index=True)
    category = Column(String(255), index=True)