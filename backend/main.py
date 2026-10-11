from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Telemetry(BaseModel):
    rpm: int
    coolant_temp: float
    oil_temp: float
    oil_pressure: float
    speed: float

@app.get("/")
def home():
    return {"message": "Q50 Telemetry API is up and running!"}

@app.get("/telemetry")
def get_telemetry():
    return {
        "rpm": 1850,
        "coolant_temp": 185,
        "oil_temp": 194,
        "oil_pressure": 22.6,
        "speed": 42
    }

@app.post("/telemetry")
def receive_telemetry(data: Telemetry):
    return {
        "message": "Telemetry received",
        "data": data
    }