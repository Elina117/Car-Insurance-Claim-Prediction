from pydantic import BaseModel

class PredictionResult(BaseModel):
    id: str
    prediction: str
    probability: str