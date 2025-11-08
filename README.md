# Como rodar a aplicação #

para ativar o ambiente virtual, no terminal coloque:
```
python -m venv venv
venv\Scripts\activate
```
---
Instale as dependencias:
```
pip install -r requirements.txt
```
---
Acesse :
```
http://127.0.0.1:8000/docs
```
---
Localize o endpoint /conteudo/ :

Clique em "Try it out"

Isso habilita os campos para edição.
Preencha o JSON de exemplo.
```
{
  "tema": "beleza",
  "tipo": "informativo",
  "objetivo": "atrair seguidores",
  "publico": "mulheres solteiras entre 20 e 30 anos",
  "tom": "casual",
  "rede_alvo": "Instagram",
  "formato": "carrossel"
}
```

