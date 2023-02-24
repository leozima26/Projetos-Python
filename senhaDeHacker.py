#4 - Um grande cliente seu sofreu um ataque hacker: o servidor foi sequestrado por um software malicioso, que criptografou todos os discos e pede a 
# digitação de uma senha para a liberação da máquina. E é claro que os criminosos exigem um pagamento para informar a senha.
# Ao analisar o código do programa deles, porém, você descobre que a senha é composta da palavra “LIBERDADE” seguida do fatorial dos minutos que 
# a máquina estiver marcando no momento da digitação da senha (se a máquina estiver marcando 5 minutos, a senha será LIBERDADE120). Crie um
#  programa que receba do usuário os minutos atuais e exiba na tela a senha necessária para desbloqueio. ATENÇÃO: seu programa não pode utilizar 
# funções prontas para o cálculo do fatorial. Ele deve obrigatoriamente utilizar loop.

n_minutos = int(input("Digite o minutos atuais de sua maquina: "))

n_contador = n_minutos
n_fatorial = 1
#FATOR NULO DE MULTIPLICAÇÃO É 1, OU SEJA, SE FOSSE 0, O RESULTADO X 0 = 0
while n_contador > 0:
    n_fatorial *= n_contador
    n_contador -= 1 
print("A senha para desbloqueio da máquina é: LIBERDADE{}".format(n_fatorial))


#FEITO E ELABORADO POR LEONARDO ZIMMERMANN ALVES UEDA RM 95192 IDE VScode

