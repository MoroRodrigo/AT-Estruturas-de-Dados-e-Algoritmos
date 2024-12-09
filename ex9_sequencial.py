# Lista sequencial de perfis
lista_usuarios = [
    {"nome_usuario": "joao123", "dados": {"nome": "João", "email": "joao@email.com"}},
    {"nome_usuario": "maria456", "dados": {"nome": "Maria", "email": "maria@email.com"}},
    {"nome_usuario": "ana789", "dados": {"nome": "Ana", "email": "ana@email.com"}}
]

# Função para buscar um perfil
def buscar_na_lista(nome_usuario):
    for usuario in lista_usuarios:
        if usuario["nome_usuario"] == nome_usuario:
            return usuario["dados"]
    return "Usuário não encontrado."

# Testando a busca
print(buscar_na_lista("joao123"))  # Deve retornar o perfil de João
print(buscar_na_lista("pedro000"))  # Deve retornar "Usuário não encontrado."
