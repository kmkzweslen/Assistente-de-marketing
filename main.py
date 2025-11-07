from fastapi import FastAPI
from app.api.conteudo import router as conteudo_router

app = FastAPI(title="API Conteúdo com LLMs")

app.include_router(conteudo_router, prefix="/conteudo", tags=["Conteudo"])
