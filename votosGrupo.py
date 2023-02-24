#Colaboradores vão ganhar um premio e será feito uma votação
#por questão de logistica, o mesmo console vencedor será distribuido para todos igualmente.
#quantidade de colaboradores: 5
#opções: xbox, playstation e nintendo
from re import A, X


voto1 = input("Colaborador 1 qual opção quer ganhar: Xbox, PlayStation ou Nintendo? ")
voto2 = input("Colaborador 2 qual opção quer ganhar: Xbox, PlayStation ou Nintendo? ")
voto3 = input("Colaborador 3 qual opção quer ganhar: Xbox, PlayStation ou Nintendo? ")
voto4 = input("Colaborador 4 qual opção quer ganhar: Xbox, PlayStation ou Nintendo? ")
voto5 = input("Colaborador 5 qual opção quer ganhar: Xbox, PlayStation ou Nintendo? ")

playstation = 0
xbox = 0
nintendo = 0

if voto1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto1.upper() == "XBOX":
    xbox = xbox + 1
elif voto1.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print (" O colaborador 1 digitou um console inexistente e seu voto foi desconsiderado") 

if voto2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto2.upper() == "XBOX":
    xbox = xbox + 1
elif voto2.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print (" O colaborador 2 digitou um console inexistente e seu voto foi desconsiderado") 

if voto3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto3.upper() == "XBOX":
    xbox = xbox + 1
elif voto3.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print (" O colaborador 3 digitou um console inexistente e seu voto foi desconsiderado") 

if voto4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto4.upper() == "XBOX":
    xbox = xbox + 1
elif voto4.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print (" O colaborador 4 digitou um console inexistente e seu voto foi desconsiderado") 

if voto5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto5.upper() == "XBOX":
    xbox = xbox + 1
elif voto5.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print (" O colaborador 5 digitou um console inexistente e seu voto foi desconsiderado") 

if playstation > xbox and playstation > nintendo:
    print("O console escolhido foi PlayStation, parabens a equipe!")
elif xbox > playstation and xbox > nintendo:
    print("O console escolhido foi Xbox, parabens a equipe!")
elif nintendo > playstation and nintendo > xbox:
    print("O console escolhido foi Nintendo, parabens a equipe!")
else:
    print("Houve empate, refazer votação ou entrar em contato com direção!")    
