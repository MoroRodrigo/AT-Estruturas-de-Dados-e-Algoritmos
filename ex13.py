def knapsack(capacidade, pesos, valores, n):
    # Criar uma tabela DP com (n+1) linhas e (capacidade+1) colunas
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Preencher a tabela DP
    for i in range(1, n + 1):
        for j in range(1, capacidade + 1):
            # Se o item i não pode ser incluído na mochila (peso[i-1] > capacidade j)
            if pesos[i - 1] > j:
                dp[i][j] = dp[i - 1][j]  # Não inclui o item i
            else:
                # Caso contrário, escolhe o melhor entre incluir ou não o item
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - pesos[i - 1]] + valores[i - 1])

    return dp[n][capacidade]

# Teste
pesos = [2, 3, 4, 5] 
valores = [3, 4, 5, 6]
capacidade = 5 
n = len(pesos)

# Chama função/ imprime o resultado
resultado = knapsack(capacidade, pesos, valores, n)
print(f"Valor máximo que pode ser carregado: {resultado}")
