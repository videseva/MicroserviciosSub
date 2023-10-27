from typing import Optional
from pydantic import BaseModel

class Notification(BaseModel):
    id: Optional[int]
    fecha :str
    asunto :str
    message:str
    email:str
