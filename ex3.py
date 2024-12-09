def buscar_contato(lista_contatos, nome_procurado):
    for contato in lista_contatos:
        if contato["nome"].lower() == nome_procurado.lower():
            return f"Contato encontrado: {contato['nome']} - Telefone: {contato['telefone']}"
    return "Contato não encontrado."

# Lista de contatos desordenada
contatos = [
    {"nome": "Ana", "telefone": "1234-5678"},
    {"nome": "Carlos", "telefone": "9876-5432"},
    {"nome": "Beatriz", "telefone": "4567-8901"},
    {"nome": "João", "telefone": "3456-7890"},
    {"nome": "Mariana", "telefone": "6789-1234"}
]

# Uso
nome_para_buscar = input("Digite o nome do contato que deseja buscar: ")
resultado = buscar_contato(contatos, nome_para_buscar)
print(resultado)
