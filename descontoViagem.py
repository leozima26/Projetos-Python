#SCRIPT PARA UMA AGENCIA DE VIAGENS
#ATRIBUINDO VALOR BRUTO, CATEGORIA DOS ASSENTOS E QUANTIDADES DE VIAJANTES
#CATEGORIAS:
#ECONOMICA 2 VIAJANTES 3%
#           3 VIAJANTES 4%
#           4 VIAJANTES OU MAIS 5%
#EXECUTIVA 2 VIAJANTES 5%
#           3 VIAJANTES 7%
#           4 VIAJANTES OU MAIS 8%
#PRIMEIRA CLASSE 2 VIAJANTES 10%
#                3 VIAJANTES 15%
#                4 VIAJANTES OU MAIS 20%

#VALOR BRUTO, VALOR DE DESCONTO, VALOR LIQUIDO DA VIAGEM E VALOR MEDIO POR VIAJANTE.

valor_bruto = float(input("Por favor, informe o valor bruto da viagem: "))
categoria = input("Por favor, informe a categoria: 1-Econômica, 2-Executiva, 3-Primeira Classe: ")
quantidades_viajantes = int(input("Por favor, informe a quantidade de viajantes: "))

if categoria.upper() == "ECONOMICA":
    if quantidades_viajantes == 2:
        valor_desconto = valor_bruto * 0.03
    elif quantidades_viajantes == 3:
        valor_desconto = valor_bruto * 0.04
    elif quantidades_viajantes >= 4:
        valor_desconto = valor_bruto * 0.05

elif categoria.upper() == "EXECUTIVA":
    if quantidades_viajantes == 2:
        valor_desconto = valor_bruto * 0.05
    elif quantidades_viajantes == 3:
        valor_desconto = valor_bruto * 0.07
    elif quantidades_viajantes >= 4:
        valor_desconto = valor_bruto * 0.08            

elif categoria.upper() == "PRIMEIRA CLASSE":
    if quantidades_viajantes == 2:
        valor_desconto = valor_bruto * 0.10
    elif quantidades_viajantes == 3:
        valor_desconto = valor_bruto * 0.15
    elif quantidades_viajantes >= 4:
        valor_desconto = valor_bruto * 0.20
else: 
    print("Categoria inexistente, não concedido nenhuma desconto!")

valor_liquido = valor_bruto - valor_desconto
media_viajante = valor_liquido / quantidades_viajantes

print("O valor da viagem é de R${}. Após os descontos de R${}, a viagem custará R${}. Cada passageiro tem um custo médio de R${}".format(valor_bruto, valor_desconto, valor_liquido, media_viajante))
