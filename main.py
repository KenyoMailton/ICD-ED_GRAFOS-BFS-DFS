# -*- coding: utf-8 -*-
from graph import Graph

def load_from(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())
    
    g = Graph(n)
    
    l = 0
    for line in f:
        line.strip()
        numeros = line.split("\t")
        c = 0
        for i in numeros:
            if(c == g.num_vertices):
                break
            g.matrix[l][c] = int(i)
            if(g.matrix[l][c] > 0):
                g.list[l].append(c)
            
            c += 1
        l += 1
    return g

def main():
    gr = load_from("pcv4.txt")
    gr.print()
    
    # vértice inicial
    start_vertex = 2
    dist = gr.bfs(start_vertex)
    print(f"Distâncias a partir do vértice {start_vertex}: {dist}")
    
    # vértice alvo
    target_vertex = 8
    path = gr.find_path(start_vertex, target_vertex)
    print(f"Caminho de {start_vertex} a {target_vertex}: {path}")
    
    print(f"Busca em Profundidade do vértice inicial {start_vertex} (DFS):")
    dfs_result = gr.dfs(start_vertex)
    print(dfs_result)

if __name__ == "__main__":
    main()
