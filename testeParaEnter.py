from audioop import reverse


inventario=[]
lista=[]
resposta = "SIM"

#adicionar item no inventario
while resposta == "SIM":
  equipamento=[int(input("Equipamento: ")),
            float(input("Valor: ")),
            input("Número Serial: ")]
  lista.append(equipamento)
  inventario.append(lista)
  resposta = input("Digite SIM para continuar, NAO para finalizar: ").upper()
#exibir dados do inventário
inventario.sort(reverse = True)
print("Nome.........: ", inventario[0])
print("Valor........: ", inventario[1])
print("Serial.......: ", inventario[2])
  
#localizar um item no inventario
busca=input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
  if busca==elemento[0]:
    print("Valor..: ", elemento[1])
    print("Serial.:", elemento[2])

#depreciar itens no inventario
depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
  if depreciacao==elemento[0]:
    print("Valor antigo: ", elemento[1])
    elemento[1] = elemento[1] * 0.9
    print("Novo valor: ", elemento[1])

#excluir um item do inventario
serial=int(input("Digite o serial do equipamento que será excluído: "))
for elemento in inventario:
  if elemento[2]==serial:
    inventario.remove(elemento)

#exibir dados do inventário
for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])

#resumo de valores do inventário
valores=[]
for elemento in inventario:
  valores.append(elemento[1])
if len(valores)>0:
  print("O equipamento mais caro custa: ", max(valores))
  print("O equipamento mais barato custa: ", min(valores))
  print("O total de equipamentos é de: ", sum(valores))