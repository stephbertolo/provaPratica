linha = []
matriz = []

def criarMatriz(linhas, colunas):
    for linha in range(linhas):
        for coluna in range(colunas):
            matriz.append(0)
    return matriz


print(criarMatriz(4, 4))

for linha in matriz:
    valorInteiro = int(input("Digite um valor inteiro: "))
