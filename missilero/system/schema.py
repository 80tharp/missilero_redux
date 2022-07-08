from pydantic import BaseModel, constr


class Category(BaseModel):
    name: constr(min_length=1, max_length=50)


class DisplayCategory(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class System(BaseModel):
    system_name: str
    system_country: str
    system_range_class: str
    system_warhead: str
    system_range: str
    system_nuke_type: str
    system_launcher: str
    system_description: str
    system_image: str
    system_type: str
    system_status: str
    category_id: int

class DisplaySystem(BaseModel):
    system_id: int
    system_name: str
    system_country: str
    system_range_class: str
    system_warhead: str
    system_range: str
    system_nuke_type: str
    system_launcher: str
    system_description: str
    system_image: str
    system_type: str
    system_status: str
    category_id: int
    category: str

    class Config:
        orm_mode = True
