import random

dado = [1, 2, 3, 4, 5, 6]

playerUm = []
playerDois = []

comecarJogo = True

escolhaJogador = int(input("Escolha 1 para começar ou 2 para encerrar: "))


def randomizarValor(jogador):
    valor = random(dado)
    jogador.append(valor)

if escolhaJogador == 1:
    comecarJogo = True
    print(f"Jogo começou. {comecarJogo}")
    randomizarValor(playerUm)
    print(playerUm)


elif escolhaJogador == 2:
    print(f"Jogo encerrou. {comecarJogo}")
    comecarJogo = False
    quit()

else:
    print("Opção inválida!")
    escolhaJogador = int(input("Escolha 1 para começar e 2 para encerrar: "))

# Não consegui fazer :(