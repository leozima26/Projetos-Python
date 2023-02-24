#Programa para verificar se os batimentos cardiacos por minutos estão adequados ou não
#Usando if compostos junto com operadores logicos AND e OR
#Idade em bpm
#Até 2 anos de idade bpm de 120 a 140
#de 3 anos a até 7 anos bpm de 100 a 130
#de 8 anos a até 17 anos bpm de 80 a 100
#de 18 anos a até 64 anos bpm de 70 a 79
#acima de 65 anos bpm de 50 a 60

from re import I


print ("VERIFICADOR DE FREQUÊNCIA CARDÍACA")
idade = int(input("Por favor informe sua idade:"))
bpm = int(input("Por favor, digite seu bpm:"))

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
            print("Batimentos normais para a idade fornecida")
    else:
        print("Batimentos fora dos indicados para a idade")

elif idade >= 3 and idade <= 7:
        if bpm >= 100 and bpm <= 130:
                print("Batimentos normais para a idade fornecida")          
        else:
            print("Batimentos fora dos indicados para a idade")

elif idade >= 8 and idade <= 17:
        if bpm >= 80 and bpm <= 100:
            print("Batimentos normais para a idade fornecida")
        else:
            print("Batimentos fora dos indicados para a idade")            

elif idade >=18 and idade <= 64:
        if bpm >= 70 and bpm <= 79:
            print("Batimentos normais para a idade fornecida")
        else:
            print("Batimentos fora dos indicados para a idade")
elif idade >= 65:
        if bpm >= 50 and bpm <= 60:
            print("Batimentos normais para a idade fornecida")
        else:
            print("Batimentos fora dos indicados para a idade")

else:
    print("Não foi possivel verificar os bpm para essa idade")                