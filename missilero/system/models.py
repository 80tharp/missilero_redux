from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship

from missilero.db import Base


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    system = relationship("System", back_populates="category")


class System(Base):
    __tablename__ = 'system'

    system_id = Column(Integer, primary_key=True, autoincrement=True)
    system_name = Column(String(50))
    system_country = Column(String(50))
    system_range_class = Column(String(15))
    system_warhead = Column(String(15))
    system_range = Column(String(15))
    system_nuke_type = Column(String(15))
    system_launcher = Column(String(15))
    system_description = Column(Text)
    system_image = Column(String(50))
    system_type = Column(String(50))
    system_status = Column(String(50))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", back_populates="system")

