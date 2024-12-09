class FilaDeAtendimento:
    def __init__(self):
        self.fila = []  # Lista que representa a fila de chamados

    def inserir_chamado(self, chamado):
        self.fila.append(chamado)
        print(f"Chamado '{chamado}' inserido na fila de atendimento.")

    def remover_chamado(self):
        if self.fila:
            chamado_atendido = self.fila.pop(0)  # Remove o primeiro chamado
            print(f"Chamado '{chamado_atendido}' atendido e removido da fila.")
            return chamado_atendido
        else:
            print("Não há chamados na fila para atendimento.")
            return None

    def exibir_fila(self):
        if self.fila:
            print("Chamados na fila de atendimento:")
            for chamado in self.fila:
                print(f"- {chamado}")
        else:
            print("Não há chamados na fila.")

# Teste sistema de atendimento
atendimento = FilaDeAtendimento()

# Inserindo chamados na fila
atendimento.inserir_chamado("Problema de login")
atendimento.inserir_chamado("Erro no sistema de pagamentos")
atendimento.inserir_chamado("Dúvida sobre a funcionalidade X")

# Exibindo a fila de chamados
atendimento.exibir_fila()

# Removendo/Atendendo os chamados
atendimento.remover_chamado()  # Esperado: "Problema de login"
atendimento.remover_chamado()  # Esperado: "Erro no sistema de pagamentos"

# Exibindo a fila após remoção
atendimento.exibir_fila()

# Tentando remover de uma fila vazia
atendimento.remover_chamado()  # Esperado: "Dúvida sobre a funcionalidade X"
atendimento.remover_chamado()  # Esperado: "Não há chamados na fila para atendimento."
