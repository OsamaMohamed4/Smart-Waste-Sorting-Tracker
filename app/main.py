from fastapi import FastAPI
import models, database
from routers import devices, sorting, reports


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Smart Waste Sorting Tracker")

app.include_router(devices.router)
app.include_router(sorting.router)
app.include_router(reports.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Smart Waste Sorting Tracker"}