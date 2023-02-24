dicionario = {}

#primeria maneira
dicionario ["Curso Udemy"] = "R$27.00"

#segunda maneira
nome_curso = input("Por favor coloque o curso desejado: ")
valor_curso = input("Por favor coloque o valor do curso: ")

dicionario [nome_curso] = valor_curso

for item, valor in dicionario.items():
    print("O {} adquirido foi no valor de {}, boas aulas!".format(item, valor))

print("")
#alterando valor de uma chave, colocando mesmo nome e simplesmente alterando o valor posteriormente
dicionario ["Curso Udemy"] = "R$27.50"

for item, valor in dicionario.items():
    print("O {} foi alterado para o valor de {}, boas aulas!".format(item, valor))

#igual listas a tag POP serve para retirar uma chave especifica junto com seu valor_curso, e .POPITEM 
#retira o ultimo item de seu dicionario

dicionario.pop("Curso Udemy")

for item, valor in dicionario.items():
    print("O {} adquirido foi no valor de {}, boas aulas!".format(item, valor))