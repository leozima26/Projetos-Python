#2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana
# é o melhor para a realização das lives. Desenvolva um programa em que o usuário 
# informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, 
# terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e 
# exiba qual dia foi o escolhido.

segunda_feira = int(input("Por favor, coloque a quantidade de votos da Segunda-Feira: "))
terca_feira = int(input("Por favor, coloque a quantidade de votos da Terça-feira: "))
quarta_feira = int(input("Por favor, coloque a quantidade de votos da Quarta-Feira: "))
quinta_feira = int(input("Por favor, coloque a quantidade de votos da Quinta-Feira: "))
sexta_feira = int(input("Por favor, coloque a quantidade de votos da Sexta-Feira: "))

if segunda_feira > terca_feira and segunda_feira > quarta_feira and segunda_feira > quinta_feira and segunda_feira > sexta_feira:
    print("O dia escolhido para realizar as lives foi Segunda-Feira!")
elif terca_feira > segunda_feira and terca_feira > quarta_feira and terca_feira > quinta_feira and terca_feira > sexta_feira:
    print("O dia escolhido para realizar as lives foi Terça-Feira!")
elif quarta_feira > segunda_feira and quarta_feira > terca_feira and quarta_feira > quinta_feira and quarta_feira > sexta_feira:
    print("O dia escolhido para realizar as lives foi Quarta-Feira!")
elif quinta_feira > segunda_feira and quinta_feira > terca_feira and quinta_feira > quarta_feira and quinta_feira > sexta_feira:
    print("O dia escolhido para realizar as lives foi Quinta-Feira!")
elif sexta_feira > segunda_feira and sexta_feira > terca_feira and sexta_feira > quarta_feira and sexta_feira > quinta_feira:
    print("O dia escolhido para realizar as lives foi Sexta-Feira!")
else:
    print("A votação houve empate, refazer votação ou acionar reitoria!") 



#FEITO E ELABORADO POR LEONARDO ZIMMERMANN ALVES UEDA RM 95192 IDE VScode
