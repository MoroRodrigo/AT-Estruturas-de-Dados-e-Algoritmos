class Nodo:
    def __init__(self, chave):
        self.chave = chave  # Preço do produto
        self.esquerda = None  # Subárvore esquerda
        self.direita = None  # Subárvore direita

class ArvoreBinariaDeBusca:
    def __init__(self):
        self.raiz = None

    # Insere preço na árvore
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

    # Buscar preço na árvore
    def buscar(self, chave):
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, nodo, chave):
        if nodo is None:
            return False  # Preço não encontrado
        if chave == nodo.chave:
            return True  # Preço encontrado
        elif chave < nodo.chave:
            return self._buscar_recursivo(nodo.esquerda, chave)
        else:
            return self._buscar_recursivo(nodo.direita, chave)

# Cria árvore e insere os preços
precos = [100, 50, 150, 30, 70, 130, 170]
arvore = ArvoreBinariaDeBusca()

# Insere os preços na árvore
for preco in precos:
    arvore.inserir(preco)

# Busca o preço 70 na árvore
preco_busca = 70
resultado_busca = arvore.buscar(preco_busca)

# Resultado
if resultado_busca:
    print(f"O preço {preco_busca} está disponível.")
else:
    print(f"O preço {preco_busca} não foi encontrado.")
