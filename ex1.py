import time

# Lista desordenada
class Produto:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

# Árvore de Busca Binária
class Nodo:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.esquerda = None
        self.direita = None

class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, id, nome):
        novo_nodo = Nodo(id, nome)
        if not self.raiz:
            self.raiz = novo_nodo
        else:
            self._inserir_recursivo(self.raiz, novo_nodo)

    def _inserir_recursivo(self, atual, novo):
        if novo.id < atual.id:
            if atual.esquerda:
                self._inserir_recursivo(atual.esquerda, novo)
            else:
                atual.esquerda = novo
        else:
            if atual.direita:
                self._inserir_recursivo(atual.direita, novo)
            else:
                atual.direita = novo

    def buscar(self, id):
        return self._buscar_recursivo(self.raiz, id)

    def _buscar_recursivo(self, atual, id):
        if not atual or atual.id == id:
            return atual
        if id < atual.id:
            return self._buscar_recursivo(atual.esquerda, id)
        return self._buscar_recursivo(atual.direita, id)


# Testando o desempenho
produtos_lista = []
arvore = ArvoreBuscaBinaria()

# Inserindo dados
for i in range(1, 1000000):
    produtos_lista.append(Produto(i, f"Produto {i}"))
    arvore.inserir(i, f"Produto {i}")

# Medindo busca na lista
inicio_lista = time.time()
encontrado = next((p for p in produtos_lista if p.id == 999999), None)
fim_lista = time.time()

# Medindo busca na árvore
inicio_arvore = time.time()
encontrado_arvore = arvore.buscar(999999)
fim_arvore = time.time()

print(f"Tempo de busca na lista: {fim_lista - inicio_lista:.5f} segundos")
print(f"Tempo de busca na árvore: {fim_arvore - inicio_arvore:.5f} segundos")
