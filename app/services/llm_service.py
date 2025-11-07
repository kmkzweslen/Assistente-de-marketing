import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def gerar_via_llm(params):
    prompt = (
        f"Gere um conteúdo para o tema '{params['tema']}', "
        f"tipo '{params['tipo']}', objetivo '{params['objetivo']}', "
        f"público '{params['publico']}', tom '{params['tom']}', "
        f"rede alvo '{params['rede_alvo']}', formato '{params['formato']}'."
    )
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, openai_api_key=openai_api_key)
    messages = [
        ("system", "Você é um assistente de marketing criativo. Responda sempre com uma linguagem adequada à rede social e ao público solicitado."),
        ("human", prompt)
    ]
    resposta = llm.invoke(messages)
    return resposta.content
