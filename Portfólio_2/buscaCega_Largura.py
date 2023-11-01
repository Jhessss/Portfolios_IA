#A busca em largura é um algoritmo de busca cega que explora todos os nós vizinhos antes de avançar para os próximos nós. Abaixo está uma implementação simples desse algoritmo.


from collections import deque  # Importa a classe 'deque' para usar uma fila.

# Função para realizar busca em largura em um grafo.
def busca_em_largura(graph, start, goal):
    # Inicializa uma fila com o nó de início e um caminho contendo apenas o nó de início.
    queue = deque([(start, [start])])
    
    # Enquanto a fila não estiver vazia, continue a busca.
    while queue:
        # Remove o primeiro elemento da fila, que contém o nó atual e o caminho até ele.
        (node, path) = queue.popleft()
        
        # Verifica se o nó atual é o nó de destino.
        if node == goal:
            return path  # Retorna o caminho até o nó de destino se encontrado.
        
        # Itera sobre os nós vizinhos do nó atual no grafo.
        for next_node in graph[node]:
            # Verifica se o nó vizinho não está no caminho atual.
            if next_node not in path:
                # Adiciona o nó vizinho à fila com o novo caminho que inclui o nó vizinho.
                queue.append((next_node, path + [next_node]))
    
    return None  # Retorna None se nenhum caminho for encontrado.

# Exemplo de uso:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_node = 'A'
goal_node = 'F'

# Chama a função de busca em largura com o grafo, o nó de início e o nó de destino.
caminho = busca_em_largura(graph, start_node, goal_node)

# Imprime o resultado, exibindo o caminho encontrado do nó de início para o nó de destino.
print(f'Caminho de {start_node} para {goal_node}: {caminho}')
