from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from collections import defaultdict
import crud, database

router = APIRouter(prefix="/reports", tags=["Reports"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.get("/summary")
def summary_report(db: Session = Depends(get_db)):
    records = crud.get_sorting_records(db)
    summary = defaultdict(float)
    for r in records:
        summary[r.waste_type] += r.weight
    return summary        