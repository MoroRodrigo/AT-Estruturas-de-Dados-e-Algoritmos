import random
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Gera listas com 1 mil e 10 mil elementos
lista_1k = [random.randint(1, 10000) for _ in range(1000)]
lista_10k = [random.randint(1, 10000) for _ in range(10000)]

# Teste algoritmo com 1 mil elementos
inicio = time.time()
bubble_sort(lista_1k)
fim = time.time()
print(f"Tempo para ordenar 1 mil elementos: {fim - inicio:.4f} segundos")

# Teste algoritmo com 10 mil elementos
inicio = time.time()
bubble_sort(lista_10k)
fim = time.time()
print(f"Tempo para ordenar 10 mil elementos: {fim - inicio:.4f} segundos")
