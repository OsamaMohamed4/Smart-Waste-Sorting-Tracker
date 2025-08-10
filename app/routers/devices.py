from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas, database




router = APIRouter(
    prefix="/devices",
      tags=["Devices"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db

    finally:
        db.close()





@router.post("/", response_model=schemas.DeviceResponse)
def create_device(device:schemas.DeviceCreate, db: Session = Depends(get_db)):
    return crud.create_device(db,device)


@router.get("/", response_model=list[schemas.DeviceResponse])
def list_device(db: Session = Depends(get_db)):
    return crud.get_devices(db)


