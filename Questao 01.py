lista = []


def criarLista():
    tamanho = int(input("Informe o tamanho da lista: "))
    for valor in range(tamanho):
        lista.append(0)
    return lista


print(criarLista())

for i in lista:
    valorInteiro = int(input("Coloque um valor inteiro para preencher a lista: "))
    lista.insert(i, valorInteiro)
    lista.pop()


print(lista)
print(list(reversed(lista)))
print(sum(lista))
print(min(lista))


