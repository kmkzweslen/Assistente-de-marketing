import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI
import asyncio

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, openai_api_key=openai_api_key)

client = OpenAI(api_key=openai_api_key)

def gerar_legenda(params):
    prompt = (
        f"Gere uma legenda para Instagram baseada no tema '{params['tema']}', "
        f"tipo '{params['tipo']}', objetivo '{params['objetivo']}', público '{params['publico']}', "
        f"tom '{params['tom']}', rede alvo '{params['rede_alvo']}', formato '{params['formato']}'."
    )
    messages = [
        ("system", "Você é um assistente de marketing criativo e sucinto."),
        ("human", prompt)
    ]
    resposta = llm.invoke(messages)
    return resposta.content

def gerar_imagem(params):
    prompt_img = (
        f"Foto ou ilustração para o tema '{params['tema']}' destinada ao público '{params['publico']}' "
        f"para uso em '{params['rede_alvo']}', formato '{params['formato']}'."
    )
    response = client.images.generate(
        prompt=prompt_img,
        model="dall-e-3",
        size="1024x1024",
        n=1,
    )
    url_imagem = response.data[0].url
    return url_imagem


def gerar_conteudo(params):
    if params['tipo'].lower() == "imagem":
        url = gerar_imagem(params) 
        legenda = gerar_legenda(params)
        return {"url_imagem": url, "legenda": legenda}
    else:
        texto = gerar_legenda(params)
        return {"texto": texto}