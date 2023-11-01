#  Abaixo está um algoritmo genético para encontrar uma solução aproximada para o problema 
# da "Mochila Multiobjetivo" (Multi-Objective Knapsack Problem). Neste problema, se tem um conjunto de itens, cada um com múltiplos objetivos (por exemplo, peso e valor), 
# e o objetivo é encontrar um conjunto de itens que maximize o valor total, sem exceder a capacidade máxima da mochila em relação ao peso.


import random  # Importa o módulo 'random' para geração de números aleatórios.

# Função para criar um indivíduo (solução inicial) aleatório para o problema da mochila.
def criar_individuo(itens, capacidade):
    # Inicializa um indivíduo com valores 0 ou 1 aleatórios para cada item.
    individuo = [random.randint(0, 1) for _ in range(len(itens))]
    
    # Garante que o peso total do indivíduo não exceda a capacidade da mochila.
    while sum([individuo[i] * itens[i]['peso'] for i in range(len(itens))]) > capacidade:
        individuo = [random.randint(0, 1) for _ in range(len(itens))]
    return individuo

# Função para calcular a aptidão de um indivíduo, ou seja, o valor e o peso de uma solução.
def calcular_aptidao(individuo, itens):
    valor = sum([individuo[i] * itens[i]['valor'] for i in range(len(itens))])
    peso = sum([individuo[i] * itens[i]['peso'] for i in range(len(itens))])
    return (valor, peso)

# Função para cruzar dois indivíduos e criar dois filhos.
def cruzar(individuo1, individuo2):
    ponto_corte = random.randint(1, len(individuo1) - 1)
    filho1 = individuo1[:ponto_corte] + individuo2[ponto_corte:]
    filho2 = individuo2[:ponto_corte] + individuo1[ponto_corte:]
    return filho1, filho2

# Função para aplicar mutação em um indivíduo com uma taxa de mutação especificada.
def mutar(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]

# Função principal que implementa o algoritmo genético para resolver o problema da mochila.
def algoritmo_genetico(itens, capacidade, tamanho_populacao, taxa_mutacao, geracoes):
    populacao = [criar_individuo(itens, capacidade) for _ in range(tamanho_populacao)]
    melhor_solucao = None

    for geracao in range(geracoes):
        # Ordena a população com base na aptidão dos indivíduos (maior valor primeiro).
        populacao = sorted(populacao, key=lambda x: calcular_aptidao(x, itens), reverse=True)
        melhor_atual = populacao[0]

        # Atualiza a melhor solução encontrada até o momento.
        if melhor_solucao is None or calcular_aptidao(melhor_atual, itens)[0] > calcular_aptidao(melhor_solucao, itens)[0]:
            melhor_solucao = melhor_atual

        nova_geracao = [melhor_atual]

        while len(nova_geracao) < tamanho_populacao:
            # Seleciona dois pais aleatórios da população e gera dois filhos por cruzamento.
            pai1, pai2 = random.choices(populacao[:5], k=2)
            filho1, filho2 = cruzar(pai1, pai2)
            mutar(filho1, taxa_mutacao)
            mutar(filho2, taxa_mutacao)
            nova_geracao.extend([filho1, filho2])

        populacao = nova_geracao

    return melhor_solucao

# Exemplo de uso:
itens = [{'peso': 2, 'valor': 8}, {'peso': 4, 'valor': 10}, {'peso': 5, 'valor': 13}, {'peso': 6, 'valor': 7}]
capacidade = 10
tamanho_populacao = 50
taxa_mutacao = 0.1
geracoes = 100
melhor_solucao = algoritmo_genetico(itens, capacidade, tamanho_populacao, taxa_mutacao, geracoes)
print(f'Melhor solução encontrada: {melhor_solucao}')
