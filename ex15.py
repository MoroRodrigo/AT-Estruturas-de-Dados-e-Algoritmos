class Nodo:
    def __init__(self, chave):
        self.chave = chave  # Nota do estudante
        self.esquerda = None  # Subárvore esquerda
        self.direita = None  # Subárvore direita

class ArvoreBinariaDeBusca:
    def __init__(self):
        self.raiz = None

    # Insere uma nota na árvore
    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = Nodo(chave)
        else:
            self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, nodo, chave):
        if chave < nodo.chave:
            if nodo.esquerda is None:
                nodo.esquerda = Nodo(chave)
            else:
                self._inserir_recursivo(nodo.esquerda, chave)
        else:
            if nodo.direita is None:
                nodo.direita = Nodo(chave)
            else:
                self._inserir_recursivo(nodo.direita, chave)

    # Buscar nota mínima na árvore
    def encontrar_minimo(self):
        return self._encontrar_minimo_recursivo(self.raiz)

    def _encontrar_minimo_recursivo(self, nodo):
        while nodo.esquerda:
            nodo = nodo.esquerda
        return nodo.chave

    # Buscar nota máxima na árvore
    def encontrar_maximo(self):
        return self._encontrar_maximo_recursivo(self.raiz)

    def _encontrar_maximo_recursivo(self, nodo):
        while nodo.direita:
            nodo = nodo.direita
        return nodo.chave

# Cria a árvore e insere as notas
notas = [85, 70, 95, 60, 75, 90, 100]
arvore = ArvoreBinariaDeBusca()

# Insere as notas na árvore
for nota in notas:
    arvore.inserir(nota)

# Encontra a nota mínima e a nota máxima
nota_minima = arvore.encontrar_minimo()
nota_maxima = arvore.encontrar_maximo()

# Resultados
print(f"A nota mínima da turma é: {nota_minima}")
print(f"A nota máxima da turma é: {nota_maxima}")
