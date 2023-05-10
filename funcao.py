from datetime import date, datetime

hoje = date.today() 


def calcular_idade(data_de_nascimento):
  if len(data_de_nascimento) != 10:
        print("Erro. Digite ex:00/00/0000")
        return -1
    

  for caracter in data_de_nascimento:
        if caracter not in '0123456789/':
            print("Erro. Digite ex:00/00/0000")
            break

  data_de_nascimento = data_de_nascimento.split('/')
    

  nascimento = {
        "dia" : int(data_de_nascimento[0]),
        "mes" : int(data_de_nascimento[1]),
        "ano" : int(data_de_nascimento[2])
    }
  
  e_mes_invalido = nascimento["mes"] < 1 or nascimento["mes"] > 12
  e_dia_invalido = nascimento["dia"] > 31 or nascimento["dia"] < 1
  
  if e_dia_invalido or e_mes_invalido:
        print("Data digitada errado")
        return -1

  idade = int(hoje.year - nascimento["ano"])

  if hoje < date(hoje.year, nascimento["mes"], nascimento["dia"]):
        idade -= 1

  return idade

   
   


#nome = ""
#while nome != "0" and nome.lower() != "zero":
  # nome = input("Nome: ")
  # print(f"seu nome é {nome}, sua idade é {idade}") 





    


