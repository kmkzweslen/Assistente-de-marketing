from fastapi import APIRouter
from app.schemas.entrada import Entrada
from app.services.llm_service import gerar_via_llm

router = APIRouter()

@router.post("/")
async def gerar_conteudo(entrada: Entrada):
    resultado = gerar_via_llm(entrada.dict())
    return {"conteudo": resultado}
