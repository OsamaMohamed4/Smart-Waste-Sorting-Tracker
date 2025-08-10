from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True)
    description = Column(String)
    sortings = relationship("SortingRecord", back_populates="device")

class SortingRecord(Base):
    __tablename__ = "sorting_records"
    id = Column(Integer, primary_key=True, index=True)
    waste_type = Column(String, index=True)  # metal, paper, plastic
    weight = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    device_id = Column(Integer, ForeignKey("devices.id"))
    device = relationship("Device", back_populates="sortings")