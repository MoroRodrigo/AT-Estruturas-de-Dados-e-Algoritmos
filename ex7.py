def verifica_duplicatas(lista):
    elementos_vistos = set()  # Conjunto usado como tabela de hash

    for elemento in lista:
        # Se o elemento já foi visto, significa que é uma duplicata
        if elemento in elementos_vistos:
            return True
        # Caso contrário, adicionamos o elemento ao conjunto
        elementos_vistos.add(elemento)
    
    # Se não houver duplicatas
    return False

# Testando
lista_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_teste_duplicada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]

print(verifica_duplicatas(lista_teste))        
print(verifica_duplicatas(lista_teste_duplicada)) 
