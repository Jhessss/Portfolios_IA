#  A busca A* é um algoritmo de busca informada que utiliza uma função heurística para estimar o custo restante até o destino, permitindo encontrar caminhos eficientes em grafos.


import heapq  # Importa o módulo 'heapq' para usar filas de prioridade (heap).

# Função para realizar a busca A* em um grafo.
def busca_a_star(graph, start, goal, h):
    # Inicializa uma fila de prioridade com uma tupla que contém o custo atual, o nó atual e o caminho até o nó atual.
    queue = [(0, start, [])]

    # Enquanto a fila de prioridade não estiver vazia, continue a busca.
    while queue:
        # Remove o elemento com o menor custo da fila de prioridade (fila heap).
        (cost, node, path) = heapq.heappop(queue)

        # Verifica se o nó atual é o nó de destino.
        if node == goal:
            return path + [node]  # Retorna o caminho até o nó de destino se encontrado.

        # Itera sobre os nós vizinhos do nó atual no grafo e seus custos associados.
        for next_node, next_cost in graph[node].items():
            # Verifica se o nó vizinho não está no caminho atual (evita ciclos).
            if next_node not in path:
                # Adiciona o nó vizinho à fila de prioridade com um novo custo calculado usando a função A*.
                # O novo custo é a soma do custo atual, o custo para chegar ao nó vizinho e uma heurística.
                # A heurística é dada por 'h[next_node]', que é a estimativa do custo restante até o nó de destino.
                # Quanto menor o custo total, mais promissor o caminho.
                heapq.heappush(queue, (cost + next_cost + h[next_node], next_node, path + [node]))

# Exemplo de uso:
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'D': 4, 'E': 3},
    'C': {'A': 1, 'F': 5},
    'D': {'B': 4},
    'E': {'B': 3, 'F': 1},
    'F': {'C': 5, 'E': 1}
}
start_node = 'A'
goal_node = 'F'

# Define uma heurística para cada nó que estima o custo restante até o nó de destino.
heuristic = {'A': 4, 'B': 2, 'C': 4, 'D': 3, 'E': 1, 'F': 0}

# Chama a função de busca A* com o grafo, o nó de início, o nó de destino e a heurística.
caminho = busca_a_star(graph, start_node, goal_node, heuristic)

# Imprime o resultado, exibindo o caminho encontrado do nó de início para o nó de destino.
print(f'Caminho de {start_node} para {goal_node}: {caminho}')
