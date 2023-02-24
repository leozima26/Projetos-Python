#em python podemos utilizar listas, retirando, acrescentando, somando, entre outras funções
#a seguir exemplos de lista e suas funuções

#apresentar lista e posição da lista (lembrando que posições começam com o zero)
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5]
print("A lista de valores fica assim: {}".format(valores))
print("A lista apresentada com posição 3 terá esse resultado: {}".format(valores[3]))
#APPEND seguifica "ACRESCENTAR" ou seja, o valor será acrescentada no ultimo da lista
valores.append(int("404"))
#Podemos colocar um valor expecifico, como podemos digitar um valor no momento que a maquina estive rodando.
valores.append(int(input("Digite um valor: ")))

#INSERT seguifica "INSERIR" ou seja, o valor será inserido e um local especifico da lista
valores.insert(2, int("222"))
#podemos também um valor especifico em uma posição especifica
valores.insert(6, int(input("Digite um valor: ")))

##NUNCA ESQUECER QUE AO COLOCAR VALORES, ELES SEMPRE SERÃO STRING, SE FOR VALORES NUNCA ESQUECER DE COLOCAR INT, FLOAT, BYTE,##
##SHORT, LONG, DOUBLE E ASSIM VAI##

#POP irá retirar o valor que estará na posição declarada
valores.pop(0) #Como a posição foi zero, na nossa lista que foi retirada o primeiro numero no caso 1
#QUANDO POP NÃO TEM DECLARADO A POSIÇÃO EXPECIFICA, ELE IRÁ RETIRAR O ULTIMO ITEM INCLUIDO NA LISTA 

#REMOVE seguifica "REMOVER" ou seja, ele irá remover um item especifico da lista
valores.remove(11)

#Outras funções que agregam nossa lista como: COUNT "CONTAR" mostra quantas vezes o item aparece na lista, 
#SORT "ORDENAR" organiza a lista em ordem crescente/alfabetica, REVERSE "REVERTER" inverte a ordem dos elementos de ums lista
contagem = valores.count(7)
print("Nesta lista o numero 7 aparece: {} vezes".format(contagem))
valores.reverse()
print("A lista agora está invertida: {}".format(valores))
valores.sort()
print("A lista agora está ordenada: {}".format(valores))

#lEN ou do ingles LENGTH "COMPRIMENTO", ou seja, irá contar quantos itens temos na lista
tamanho = len(valores)
print("A lista tem {} elementos".format(tamanho))

#SUM "SOMATÓRIA", ou seja, ele irá somar todos os elementos da lista
soma = sum(valores)
print("A soma dos elementos é {}".format(soma))

#para cada loop que o sistema der, ele vai apresentar cada valor da variavel VALORES, (nome é uma variavel também X)
for nome in valores:
    print(nome)
