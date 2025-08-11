# ♻️ Smart Waste Sorting Tracker

A **FastAPI** project for managing and tracking smart waste sorting devices.  
The system helps municipalities and recycling companies register devices,  
log sorting operations (waste type, weight, and location),  
and generate reports summarizing waste quantities by type.

---

## 🚀 Features
- Register smart waste sorting devices with location details.
- Log sorting operations for each device (waste type, weight).
- View summary reports of collected quantities per waste type.
- Auto-generated interactive documentation via **Swagger UI**.

---

## 🛠️ Requirements
- Python 3.10 or higher
- FastAPI
- Uvicorn
- SQLAlchemy (if using SQL)
- SQLite (default) or any other SQL database

---

## 📦 Installation & Run
1. **Clone the repository**
```bash
git clone https://github.com/username/smart-waste-tracker.git
cd smart-waste-tracker

## 📦 Installation & Run

### 1️⃣ Create a virtual environment
```bash
conda create -n smart_tracker python=3.10

2️⃣ Activate the environment
On Windows:

conda activate smart_tracker


On Mac/Linux:

conda activate smart_tracker

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run the server

uvicorn app.main:app --reload

5️⃣ Open Swagger UI
In your browser, go to:
http://127.0.0.1:8000/docs



