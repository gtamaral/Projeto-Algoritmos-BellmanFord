# ===========bibliotecas==========
import sys
import csv
import pandas as pd

# =============algoritmo================
class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

class Graph:
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.edges = []

    def add_edge(self, source, destination, weight):
        self.edges.append(Edge(source, destination, weight))

def bellman_ford(graph, start_vertex, end_vertex):
    # Inicializa as distâncias de todos os vértices com infinito
    distance = [float('inf')] * graph.numVertices
    # Define a distância do vértice inicial como 0
    distance[start_vertex] = 0
    # Inicializa o vetor de predecessores com None para todos os vértices
    predecessor = [None] * graph.numVertices

    # Relaxamento das arestas
    for i in range(graph.numVertices - 1):
        for edge in graph.edges:
            try:
                if distance[edge.source] + edge.weight < distance[edge.destination]:
                    distance[edge.destination] = distance[edge.source] + edge.weight
                    predecessor[edge.destination] = edge.source
            except IndexError:
                pass
    # Verifica se há ciclo negativo
    for edge in graph.edges:
        try:
            if distance[edge.source] + edge.weight < distance[edge.destination]:
                print("O grafo contém ciclo negativo")
                sys.exit()
        except IndexError:
            pass
    # Construção do caminho mínimo
    path = []
    current_vertex = end_vertex
    while current_vertex is not None:
        try:
            path.append(current_vertex)
            current_vertex = predecessor[current_vertex]
        except IndexError:
            pass
    path.reverse()

    # Retorna a distância mínima e o caminho mínimo
    return distance[end_vertex], path

#=====================================================================
# Leitura da base de dados com pandas
data = pd.read_csv('BaseDeDados.csv') #==> escrever aqui o diretorio que ta o arquivo do da bse de dados 

# Cria o grafo a partir dos dados da base
graph = Graph(numVertices=1899) 

with open('BaseDeDados.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader) # pula a primeira linha do arquivo (cabeçalho)
    for row in reader:
        graph.add_edge(int(row[0]), int(row[1]), int(row[2]))

# =================================================
# =========== input ===============================

print('='*60)
print('ALGORITMO PARA VERIFICAR A CONEXÃO ENTRE DOIS USUÁRIOS')
print('='*60)


start_vertex = int(input('digite o usuario de partida: '))
end_vertex = int(input('Digite o usuario final: '))
# Chama a função Bellman-Ford para calcular a distância mínima e o caminho mínimo
distance, path = bellman_ford(graph, start_vertex, end_vertex)

# Imprime os resultados
print('='*60)
print(f"A distância mínima do vértice {start_vertex} ao vértice {end_vertex} é {distance}")
print(f"O caminho mínimo é {path}")
