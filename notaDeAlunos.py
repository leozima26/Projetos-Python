#3 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês 
# JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: 
# o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que 
# têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas 
# teve a maior nota.
#Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas deve ser exibida uma mensagem no 
# seguinte padrão:
#VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
#POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.

quantidade_alunos = 50
nota_totalPar = 0
nota_totalImp = 0

for x in range(1,quantidade_alunos +1, 2):
    #para cada volta do loop, solicitar a nota do aluno
    nota_atualImp = int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES")
    #para cada nota solicitada, somar com a total
    nota_totalImp = nota_totalImp + nota_atualImp
    #ao final do loop, calcular a média aritmética
media_imp = nota_totalImp/ 25
print("A média da nota do grupo Impar é de {}: ".format(media_imp))

for y in range(2,quantidade_alunos +1, 2):
    nota_atualPar = int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(y)))
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    nota_totalPar = nota_totalPar + nota_atualPar
    media_par = nota_totalPar / 25
print("A média da nota do grupo Par é de {}: ".format(media_par))

if media_par > media_imp:
    print("Grupo dos alunos numero par teve uma nota média maior")
elif media_imp > media_par:
    print("Grupo dos alunos numero impar teve uma nota média maior")
else:
    print("Os dois grupos obtiveram a mesma média")    


#FEITO E ELABORADO POR LEONARDO ZIMMERMANN ALVES UEDA RM 95192 IDE VScode