# Criação hashtable
usuarios = {
    "joao123": {"nome": "João", "email": "joao@email.com"},
    "maria456": {"nome": "Maria", "email": "maria@email.com"},
    "ana789": {"nome": "Ana", "email": "ana@email.com"}
}

# Função para buscar um perfil
def buscar_perfil(nome_usuario):
    if nome_usuario in usuarios:
        return usuarios[nome_usuario]
    else:
        return "Usuário não encontrado."

# Testando busca
print(buscar_perfil("joao123"))  # Deve retornar o perfil de João
print(buscar_perfil("pedro000"))  # Deve retornar "Usuário não encontrado."
