from numpy import random

print("Jogo: Roll the dice! v1")

iniciar_jogo = input("Lançar o dado? \n")

while iniciar_jogo == "Sim" or iniciar_jogo == "s" or iniciar_jogo == "sim" or iniciar_jogo == "S":
        dado = random.randint(1, 6)
        print("Dado lançado e o valor deu...", dado)
        iniciar_jogo = input("Deseja jogar novamente? \n")
else:
    print("Jogo encerrado")