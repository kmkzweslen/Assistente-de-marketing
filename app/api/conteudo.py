from fastapi import APIRouter
from app.schemas.entrada import Entrada
from app.services.llm_service import gerar_conteudo as gerar_conteudo_service

router = APIRouter()

@router.post("/")
async def gerar_conteudo_route(entrada: Entrada):
    resultado = gerar_conteudo_service(entrada.dict()) 
    return resultado
