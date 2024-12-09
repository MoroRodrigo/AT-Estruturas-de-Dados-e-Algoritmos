from collections import deque

# Fila
class FilaDePacotes:
    def __init__(self):
        self.fila = deque()

    def adicionar_pacote(self, pacote):
        self.fila.append(pacote)  # Adiciona ao final da fila
        print(f"Pacote {pacote} adicionado à fila.")

    def processar_pacote(self):
        if self.fila:
            pacote = self.fila.popleft()  # Remove do início da fila
            print(f"Pacote {pacote} processado.")
            return pacote
        else:
            print("Nenhum pacote na fila para processar.")
            return None

# Pilha
class PilhaDePacotes:
    def __init__(self):
        self.pilha = []

    def adicionar_pacote(self, pacote):
        self.pilha.append(pacote)  # Adiciona ao topo da pilha
        print(f"Pacote {pacote} adicionado à pilha.")

    def processar_pacote(self):
        if self.pilha:
            pacote = self.pilha.pop()  # Remove do topo da pilha
            print(f"Pacote {pacote} processado.")
            return pacote
        else:
            print("Nenhum pacote na pilha para processar.")
            return None

# Testando
print("Simulando fila:")
fila = FilaDePacotes()
fila.adicionar_pacote("Pacote 1")
fila.adicionar_pacote("Pacote 2")
fila.adicionar_pacote("Pacote 3")
fila.processar_pacote()
fila.processar_pacote()

print("\nSimulando pilha:")
pilha = PilhaDePacotes()
pilha.adicionar_pacote("Pacote A")
pilha.adicionar_pacote("Pacote B")
pilha.adicionar_pacote("Pacote C")
pilha.processar_pacote()
pilha.processar_pacote()
