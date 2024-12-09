class Nodo:
    def __init__(self, chave):
        self.chave = chave  # Código do produto
        self.esquerda = None  # Subárvore esquerda
        self.direita = None  # Subárvore direita

class ArvoreBinariaDeBusca:
    def __init__(self):
        self.raiz = None

    # Insere código de produto na árvore
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

    # Remove um nó
    def remover(self, chave):
        self.raiz = self._remover_recursivo(self.raiz, chave)

    def _remover_recursivo(self, nodo, chave):
        if nodo is None:
            return nodo

        if chave < nodo.chave:
            nodo.esquerda = self._remover_recursivo(nodo.esquerda, chave)
        elif chave > nodo.chave:
            nodo.direita = self._remover_recursivo(nodo.direita, chave)
        else:
            # Caso 1: Nó folha (sem filhos)
            if nodo.esquerda is None and nodo.direita is None:
                return None

            # Caso 2: Nó com um filho
            elif nodo.esquerda is None:
                return nodo.direita
            elif nodo.direita is None:
                return nodo.esquerda

            # Caso 3: Nó com dois filhos
            else:
                sucessor = self._encontrar_minimo(nodo.direita)
                nodo.chave = sucessor
                nodo.direita = self._remover_recursivo(nodo.direita, sucessor)
        
        return nodo

    # Encontra o nó com o menor valor
    def _encontrar_minimo(self, nodo):
        while nodo.esquerda:
            nodo = nodo.esquerda
        return nodo.chave

    # Imprime a árvore em ordem crescente
    def exibir_em_ordem(self):
        self._exibir_em_ordem_recursivo(self.raiz)
        print()

    def _exibir_em_ordem_recursivo(self, nodo):
        if nodo:
            self._exibir_em_ordem_recursivo(nodo.esquerda)
            print(nodo.chave, end=" ")
            self._exibir_em_ordem_recursivo(nodo.direita)

# Cria a árvore e insere os códigos dos produtos
produtos = [45, 25, 65, 20, 30, 60, 70]
arvore = ArvoreBinariaDeBusca()

# Insere os códigos na árvore
for produto in produtos:
    arvore.inserir(produto)

# Exibe a árvore antes das remoções
print("Árvore antes das remoções:")
arvore.exibir_em_ordem()

# Remove o código 20 (nó folha)
arvore.remover(20)
print("Árvore após remover o código 20 (nó folha):")
arvore.exibir_em_ordem()

# Remove o código 25 (nó com um filho)
arvore.remover(25)
print("Árvore após remover o código 25 (nó com um filho):")
arvore.exibir_em_ordem()

# Remove o código 45 (nó com dois filhos)
arvore.remover(45)
print("Árvore após remover o código 45 (nó com dois filhos):")
arvore.exibir_em_ordem()
