#1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: um serviço em que as pessoas
#  possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema 
# de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano. Sua tarefa é criar 
# um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve 
# pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:
# Nível
# Porcentagem sobre o faturamento
# Basic 30%
# Silver 20%
# Gold 10%
# Platinum 5%

print("Planos de serviços: BASIC, SILVER, GOLD, PLATINUM")

ass_cliente = input("Por favor, escreva o plano escolhido: ")
fat_anual = float(input("Por favor, digite o faturamento anual (não usando virgula): R$"))

if ass_cliente.upper() == "BASIC":
    valor_bonus = fat_anual * 0.3
    print("O porcentagem do plano sobre o faturamento será de: 30%")
elif ass_cliente.upper() == "SILVER":
    valor_bonus = fat_anual * 0.2
    print("O porcentagem do plano sobre o faturamento será de: 20%")
elif ass_cliente.upper() == "GOLD":
    valor_bonus = fat_anual * 0.1
    print("O porcentagem do plano sobre o faturamento será de: 10%")
elif ass_cliente.upper() == "PLATINUM":
    valor_bonus = fat_anual * 0.05
    print("O porcentagem do plano sobre o faturamento será de: 5%")
else:
    print("O plano não reconhecido.")    

print("O valor do plano escolhido ficará R${}".format(valor_bonus))


#FEITO E ELABORADO POR LEONARDO ZIMMERMANN ALVES UEDA RM 95192 IDE VScode
