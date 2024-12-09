class Navegador:
    def __init__(self):
        self.pilha_voltar = []  # Pilha  histórico de páginas visitadas
        self.pilha_avancar = []  # Pilha paginas avançadas

    def visitar_pagina(self, pagina):
        """
        Quando o usuário visita uma nova página, empilha a página atual na pilha de 'voltar'
        e limpa a pilha de 'avançar' (pois não há páginas para avançar).
        """
        if self.pilha_voltar:
            self.pilha_voltar.append(pagina)
        else:
            self.pilha_voltar = [pagina]
        self.pilha_avancar.clear()  # Limpa a pilha de avançar
    def voltar(self):
        """
        Simula o botão 'Voltar'. Move a página atual da pilha de 'voltar' para 'avançar'.
        """
        if self.pilha_voltar:
            pagina_atual = self.pilha_voltar.pop()
            self.pilha_avancar.append(pagina_atual)  # Coloca a página atual na pilha de avançar
            if self.pilha_voltar:
                return self.pilha_voltar[-1]  # Retorna página atual
            else:
                return "Nenhuma página para voltar."  # Caso não haja mais páginas
        else:
            return "Nenhuma página para voltar."

    def avancar(self):
        """
        Simula o botão 'Avançar'. Move a página da pilha de 'avançar' de volta para a pilha de 'voltar'.
        """
        if self.pilha_avancar:
            pagina_atual = self.pilha_avancar.pop()
            self.pilha_voltar.append(pagina_atual) 
            return pagina_atual  # Retorna a nova página atual
        else:
            return "Nenhuma página para avançar."

# Teste sistema de navegação
navegador = Navegador()

# Usuário visita páginas
navegador.visitar_pagina("Página Inicial")
navegador.visitar_pagina("Sobre")
navegador.visitar_pagina("Contato")

# Usuário clica "Voltar"
print(navegador.voltar())  # Esperado: "Sobre"
print(navegador.voltar())  # Esperado: "Página Inicial"

# Usuário clica "Avançar"
print(navegador.avancar())  # Esperado: "Sobre"

# Usuário volta mais uma vez e tenta avançar
print(navegador.voltar())  # Esperado: "Página Inicial"
print(navegador.avancar())  # Esperado: "Sobre"
