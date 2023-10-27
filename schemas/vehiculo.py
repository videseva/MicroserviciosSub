from typing import Optional
from pydantic import BaseModel

class Vehiculo(BaseModel):
    id: Optional[int]
    fecha :str
    hora :str
    nombre: str
    email :str
    celular: str
    tipoVehiculo: str
    matricula:str
    totalPagar:str
