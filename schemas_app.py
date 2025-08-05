from pydantic import BaseModel
from datetime import datetime

class EventoCreate(BaseModel):
    id_unidad: int
    pasajeros: int

class OcupacionOut(BaseModel):
    id_unidad: int
    nombre_unidad: str
    total_pasajeros: int

    model_config = {
        "from_attributes": True
    }

class AlertaOut(BaseModel):
    mensaje: str
    nivel: str
    timestamp: datetime

    model_config = {
        "from_attributes": True
    }
