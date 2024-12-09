import time

def soma_uma_passada(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma

def soma_duas_passadas(lista):
    # Primeira passada: apenas copia os elementos
    temp = [num for num in lista]
    # Segunda passada: calcula a soma
    soma = 0
    for num in temp:
        soma += num
    return soma

# Lista de teste com 10 milhões de elementos
lista_teste = list(range(1, 10_000_001))

# Medindo o tempo do primeiro algoritmo
inicio = time.time()
resultado1 = soma_uma_passada(lista_teste)
tempo1 = time.time() - inicio

# Medindo o tempo do segundo algoritmo
inicio = time.time()
resultado2 = soma_duas_passadas(lista_teste)
tempo2 = time.time() - inicio

# Comparando resultados
print(f"Soma (1 passada): {resultado1}, Tempo: {tempo1:.4f} segundos")
print(f"Soma (2 passadas): {resultado2}, Tempo: {tempo2:.4f} segundos")
