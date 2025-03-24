graph = {
    "a":["b","d"],
    "b":[],
    "c":[],
    "d":["e","g"],
    "e":["c"],
    "f":[],
    "g":["f"]
}

def bfs(graph,source):
    queue = []
    queue.append(source)
    while queue:
        node = queue.pop(0)
        print(node)
        for neigh in graph[node]:
            queue.append(neigh)

def dfs(graph,source):
    stack = []
    stack.append(source)
    while stack:
        node = stack.pop(-1)
        print(node)
        for neigh in graph[node]:
            stack.append(neigh)

# dfs(graph,'a')

list = [[] for n in range(4)]
print(list)

