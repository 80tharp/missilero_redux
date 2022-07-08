from fastapi import HTTPException, status
from typing import List, Optional
from . import models


async def create_new_category(request, database):
    new_category = models.Category(name=request.name)
    database.add(new_category)
    database.commit()
    database.refresh(new_category)
    return new_category


async def all_categories(database) -> List[models.Category]:
    categories = database.query(models.Category).all()
    return categories


async def create_new_system(request, database):
    new_system = models.System(
        system_name=request.system_name,
        system_country=request.system_country,
        system_range_class=request.system_range_class,
        system_warhead=request.system_warhead,
        system_range=request.system_range,
        system_nuke_type=request.system_nuke_type,
        system_launcher=request.system_launcher,
        system_description=request.system_description,
        system_image=request.system_image,
        system_type=request.system_type,
        system_status=request.system_status,
    )
    database.add(new_system)
    database.commit()
    database.refresh(new_system)
    return new_system


async def get_all_systems(database) -> List[models.System]:
    systems = database.query(models.System).all()
    return systems


async def get_system_by_id(systems_id, database) -> Optional[models.System]:
    system_info = database.query(models.System).get(systems_id)
    if not system_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='data not found')
    return system_info