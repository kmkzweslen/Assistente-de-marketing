from pydantic import BaseModel

class Entrada(BaseModel):
    tema: str
    tipo: str
    objetivo: str
    publico: str
    tom: str
    rede_alvo: str
    formato: str
