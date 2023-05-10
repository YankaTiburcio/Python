from data_de_nascimento_biblioteca import calcular_idade 
import json

arquivo = open("arquivo.json", "r", encoding="utf-8")  # read = ler
dicionario = json.load(arquivo)

for i in dicionario:
    nome =  i['nome']

    if nome.lower() == "zero" or nome == "0":
        continue

    nascimento = i['nascimento']

    idade = calcular_idade(nascimento)
    
    if idade < 0:
        continue

    print(nome, idade)   

print("FIM")


pergunta = input("Deseja inserir mais um nome e data de nascimento? ")
if pergunta.lower() == "sim":
    nome = input()
    nascimento = input()

    dicionario.append({
        "nome": nome,
        "nascimento": nascimento
    })

arquivo = open("arquivo.json", "w", encoding="utf-8")  # write = escrever
arquivo.write(json.dumps(dicionario, indent=4))
