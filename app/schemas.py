from pydantic import BaseModel
from datetime import datetime
from typing import List , Optional


class SortingRecordBase(BaseModel):
    waste_type : str 
    weight : float 
    device_id : int 


class SortingRecordCreate(SortingRecordBase):
    pass 


class SortingRecordResponse(SortingRecordBase):
    id : int 
    timestamp : datetime
    class config:
        orm_mode =True 


class DeviceBase(BaseModel):
    location : str
    description: Optional[str] = None 


class DeviceCreate(DeviceBase):
    pass 


class DeviceResponse(DeviceBase):
    id : int 
    Sorting: List[SortingRecordBase] = [ ]

    class config:
        orm_mode =True

