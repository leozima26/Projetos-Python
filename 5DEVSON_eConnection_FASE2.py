#Desafio - ENTERPRISECONNECTION FASE 2
#O desafio será a criação de um ranking de criticidade de violações/vazamentos “breaches” de dados pessoais em serviços de internet,
#por meio dos critérios de dados comprometidos como senha, ajuda da senha, número do telefone, nomes, e-mail e data do vazamento.

print("..::ESSE É UM RANKING DE CRITICIDADE DE BREACHES, VOCÊ IRÁ COLOCAR AS INFORMAÇÕES SOBRE AS EMPRESAS ESCOLHIDAS::..")
print("..::O PESO DE CRITICIDADE DE BREACHES: SENHA = 5, DICA DE SENHA = 4, NÚMERO DE TELEFONE = 3, NOMES = 2, EMAIL = 1::..")
print("..::QUANDO FOR PEDIDO 'VAZAMENTO MAIS CRITICO' DEVE-SE COLOCAR O NUMERAL CORRESPONDETE AO INDICE ACIMA::..")

data = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

empresa1 = [int(input("Vazamento mais critico empresa 1: ")), 
(input("Data do vazamento AAAA-MM: ")),
input("Digite o nome da empresa: ")]
list1.append(empresa1)
data.append(list1)

empresa2 = [int(input("Vazamento mais critico empresa 2: ")), 
(input("Data do vazamento AAAA-MM: ")),
input("Digite o nome da empresa: ")]
list2.append(empresa2)
data.append(list2)

empresa3 = [int(input("Vazamento mais critico empresa 3: ")), 
(input("Data do vazamento AAAA-MM: ")),
input("Digite o nome da empresa: ")]
list3.append(empresa3)
data.append(list3)

empresa4 = [int(input("Vazamento mais critico empresa 4: ")), 
(input("Data do vazamento AAAA-MM: ")),
input("Digite o nome da empresa: ")]
list4.append(empresa4)
data.append(list4)

empresa5 = [int(input("Vazamento mais critico empresa 5: ")), 
(input("Data do vazamento AAAA-MM: ")),
input("Digite o nome da empresa: ")]
list5.append(empresa5)
data.append(list5)

data.sort(reverse = True)
print("RESULTADO DO RANKING: ")
print("Primeira empresa.......:", data[0])
print("Segunda empresa........:", data[1])
print("Terceira empresa.......:", data[2])
print("Quarta empresa.........:", data[3])
print("Quinta empresa.........:", data[4])


#ESTE PROJETO FOI ELABORADO PELA EQUIPE 5DEVSON, DO CURSO DE ANALISE E DESENVOLVIMENTO DE SISTEMAS DA FIAP - 1TDSOA
