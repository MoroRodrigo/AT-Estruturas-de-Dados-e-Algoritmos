def selection_sort(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        menor_indice = i
        for j in range(i + 1, tamanho):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        # Troca os elementos
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    return lista

# Teste algoritmo
pontuacoes = [50, 30, 70, 10, 90]
print("Lista original:", pontuacoes)
lista_ordenada = selection_sort(pontuacoes)
print("Lista ordenada:", lista_ordenada)
