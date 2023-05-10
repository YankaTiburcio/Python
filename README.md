import json

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from data_de_nascimento_biblioteca import calcular_idade 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def ler_arquivo():
    arquivo = open("arquivo.json", "r", encoding="utf-8")  # read = ler
    dicionario = json.load(arquivo)

    texto = ""

    for i in dicionario:
        nome =  i['nome']

        if nome.lower() == "zero" or nome == "0":
            continue

        nascimento = i['nascimento']

        idade = calcular_idade(nascimento)
        
        if idade < 0:
            continue

        texto += nome + " " + str(idade) + """
        """   

    return texto
