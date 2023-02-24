#LISTA COM MENU INTERATIVO PARA PROFESSORES COLOCAREM AS NOTAS DOS ALUNOS

notas = []

opcao = -1
while opcao!=4:
    print("1 - Informar notas \n2 - Exibir notas \n3 - Calcular média \n4 - sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao==1:
        notas.append(float(input("Digite a nota!")))
    elif opcao==2:
        for x in notas:
            print(x)
    elif opcao==3:
        print(sum(notas)/(len(notas)))