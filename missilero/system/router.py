from typing import List

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from missilero import db
from . import schema
from . import services
from . import validator

router = APIRouter(
    tags=['System'],
    prefix='/system'
)


@router.post('/category', status_code=status.HTTP_201_CREATED)
async def create_category(request: schema.Category, database: Session = Depends(db.get_db)):
    new_category = await services.create_new_category(request, database)
    return new_category


@router.get('/category', response_model=List[schema.DisplayCategory])
async def get_all_categories(database: Session = Depends(db.get_db)):
    return await services.all_categories(database)


@router.post('/system', status_code=status.HTTP_201_CREATED)
async def create_system(request: schema.System, database: Session = Depends(db.get_db)):
    new_system = await services.create_new_system(request, database)
    return new_system


@router.get('/systems', response_model=List[schema.DisplayCategory])
async def get_all_systems(database: Session = Depends(db.get_db)):
    return await services.get_all_systems(database)


@router.get('/system/{system_id}', response_model=List[schema.DisplayCategory])
async def get_system_by_id(system_id: int, database: Session = Depends(db.get_db)):
    return await services.get_system_by_id(system_id, database)
