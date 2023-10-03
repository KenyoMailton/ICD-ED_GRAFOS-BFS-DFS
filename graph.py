# -*- coding: utf-8 -*-
import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.list = [[] for _ in range(n)]
        

    def print(self):
        print("Matriz de Adjacência:")
        for row in self.matrix:
            print(row)
        
        print("\nLista de Adjacência:")
        for i, adj_list in enumerate(self.list):
            print(f"Vertice {i}: {adj_list}")
        
        
    def bfs(self, start_vertex):
        dist = [-1 for _ in range(self.num_vertices)]
        ant = [-1 for _ in range(self.num_vertices)]
        isVisited = [False for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(start_vertex)
        isVisited[start_vertex] = True
        dist[start_vertex] = 0
        
        while Q.empty() != True:
            p = Q.get()
            
            for v in self.list[p]:
                if isVisited[v] == False:
                    dist[v] = dist[p] + 1
                    ant[v] = p
                    Q.put(v)
                    isVisited[v] = True
        
        return dist, ant
    

    # Encontra o caminho entre os 2 vertices usando BFS
    def find_path(self, start_vertex, end_vertex):
        dist, ant = self.bfs(start_vertex)
        
        if end_vertex < 0 or end_vertex >= self.num_vertices or dist[end_vertex] == -1:
            return "Não há caminho entre os vértices."
        
        path = []
        current_vertex = end_vertex
        while current_vertex != start_vertex:
            path.append(current_vertex)
            current_vertex = ant[current_vertex]
        
        path.append(start_vertex)
        path.reverse()
        return path
    

    # Busca em profundidade 
    def dfs(self, start_vertex): 
        visited = [False for _ in range(self.num_vertices)]
        stack = [start_vertex]
        result = []
        
        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                visited[vertex] = True
                result.append(vertex)
                for neighbor in reversed(self.list[vertex]):
                    if not visited[neighbor]:
                        stack.append(neighbor)
        
        return result
