from sqlalchemy.orm import session
import models , schemas



def create_device (db : session, device:schemas.DeviceCreate):
    db_device = models.Device(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

def get_devices(db : session):
    return db.query(models.Device).all()


def create_sorting_record(db:session, record:schemas.SortingRecordCreate):
    db_record = models.SortingRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_sorting_record(db : session):
    return db.query(models.SortingRecord).all()


def get_summary_report(db : session):
    return db.query(models.SortingRecord.waste_type,
                    models.SortingRecord.weight).all()


