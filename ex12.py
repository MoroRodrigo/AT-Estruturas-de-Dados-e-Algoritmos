import os

def listar_arquivos(diretorio):
    # Lista conteúdo do diretório fornecido
    try:
        conteudo = os.listdir(diretorio)
    except PermissionError:
        print(f"Acesso negado ao diretório: {diretorio}")
        return
    except FileNotFoundError:
        print(f"O diretório {diretorio} não existe.")
        return

    # Iteran sobre os itens encontrados no diretório
    for item in conteudo:
        caminho_completo = os.path.join(diretorio, item)
        
        # Verifica se é um arquivo
        if os.path.isfile(caminho_completo):
            print(caminho_completo)  # Imprime o caminho completo do arquivo
        # Se for um diretório, chama recursivamente a função
        elif os.path.isdir(caminho_completo):
            listar_arquivos(caminho_completo)

# Teste
diretorio_inicial = "C:/Users/rodri"
listar_arquivos(diretorio_inicial)
