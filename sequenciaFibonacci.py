#usando a sequencia de Fibonacci o usuario deve acertar um numero da sequencia e mostrar que o resultado foi bem sucedido
#caso contrario devera aparecer uma msg dizendo que a ação nao foio bem sucedida pois o numero não pertence a sequencia

numero_usuario = int(input("Por favor, informe um número inteiro: "))

quantidade_elementos = 10
anterior1 = 0
anterior2 = 1

for n_elemento in range(1, quantidade_elementos +1, 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual
    if numero_usuario == atual:
        print("Ação bem sucedida")
        break
    elif numero_usuario < atual:
        print("Ação Falhou!")
        break
