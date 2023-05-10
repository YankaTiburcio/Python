from data_de_nascimento_biblioteca import calcular_idade

#nome = input("nome: ")
import json

arquivo = open("arquivo.json", "r", encoding="utf-8")

dicionario = list(json.load(arquivo))



for i in dicionario:
    nome = i['nome']
    nascimento = i['nascimento']

    while nome.lower() != "zero" and nome != "0" :
     nascimento = input()
     idade = calcular_idade(nascimento)
     if not calcular_idade (nome):
        continue

    nome = input("Nome: ")

print('fim!')    
