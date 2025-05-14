from pydantic import BaseModel
from typing import Dict

class InputData(BaseModel):
    features: Dict[str, float]

class PredictionResult(BaseModel):
    prediction: float
