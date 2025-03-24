from graphInDsa.Graph1 import graph


class AdjacencyList:
     def build_graph(self,edges,n):
        graph = [[] for i in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return graph
class AdjacencyMatrix:
    def print_graph(self,grid,n):
        for i in range(n):
            print(i,end=' : ')
            for j in range(n):
                if grid[i][j] == 1:
                    print(j,end=' ')
            print()

# class AdjacencyMatrix:
#     def print_graph(self, grid, n):
#         for i in range(n):
#             connections = [str(j) for j in range(n) if grid[i][j] == 1]
#             print(f"{i} : {' '.join(connections)}")

# if __name__ == '__main__':
#     edges = [[0,1],[0,2],[1,2],[1,3],[1,4],[2,5],[3,4],[3,5]]
#     n = 6
#     adjacentList = AdjacencyList()
#     graph = adjacentList.build_graph(edges, n)
#     for i in range(n):
#         print(i,end=" : ")
#         for nbr in graph[i]:
#             print(nbr,end= " ")
#         print()

if __name__ == '__main__':
    grid = [
        [0,1,1,0,0,0],
        [1,0,1,1,1,0],
        [1,1,0,0,0,1],
        [0,1,0,0,1,1],
        [0,1,0,1,0,0],
        [0,0,1,1,0,0]
    ]
    n = 6

    adjacencyMatrix = AdjacencyMatrix()
    adjacencyMatrix.print_graph(graph,n)