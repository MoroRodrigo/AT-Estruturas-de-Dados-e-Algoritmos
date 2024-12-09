import random

def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    iteracoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        iteracoes += 1

        if lista[meio] == alvo:
            return meio, iteracoes
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, iteracoes


def busca_linear(lista, alvo):
    iteracoes = 0

    for i in range(len(lista)):
        iteracoes += 1
        if lista[i] == alvo:
            return i, iteracoes

    return -1, iteracoes


# Criando uma lista ordenada de 100 mil ISBNs fictícios
isbn_lista = sorted(random.sample(range(1_000_000, 2_000_000), 100_000))

# Escolhendo um ISBN aleatório para busca
isbn_alvo = random.choice(isbn_lista)

# Testando busca binária
indice_binaria, iteracoes_binaria = busca_binaria(isbn_lista, isbn_alvo)

# Testando busca linear
indice_linear, iteracoes_linear = busca_linear(isbn_lista, isbn_alvo)

# Resultados
print(f"Busca Binária -> Índice: {indice_binaria}, Iterações: {iteracoes_binaria}")
print(f"Busca Linear  -> Índice: {indice_linear}, Iterações: {iteracoes_linear}")
