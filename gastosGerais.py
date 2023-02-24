#o usuario ira informar quantas transações foram feitas ao longo do dia
#valor de cada uma das transações
#no final deve exibir valor total gasto e a meia entre transações

quantidade_transacoes = int(input("Informe a quantidade de transações: "))
total_transacoes = 0
for n_transacoes in range(1, quantidade_transacoes + 1, 1):
    transacao = float(input("Por favor informe a transação de {}: ".format(n_transacoes)))
    total_transacoes = total_transacoes + transacao

media = total_transacoes / quantidade_transacoes
print("Neste dia teve um gasto de R${}, com uma média de R${} por transação.".format(total_transacoes, media))    