from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas, database


router = APIRouter(prefix="/sorting", tags=["Sorting"])



def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.SortingRecordResponse)
def create_sorting_record(record:schemas.SortingRecordCreate, db: Session = Depends(get_db)):
    return crud.create_sorting_record(db, record)


@router.get("/", response_model=list[schemas.SortingRecordResponse])
def list_sorting_records(db: Session = Depends(get_db)):
    return crud.get_sorting_record(db)