def dfs(V):
    if visited_dfs[V] == False:
        DFS.append(V)
    visited_dfs[V] = True
    for i in sorted(stack[V]):
        if visited_dfs[i] == False:
            dfs(i)

def bfs(V):
    Q = []
    # if visited_bfs[V] == False:
    #     BFS.append(V)
    visited_bfs[V] = True
    Q.append(V)
    while Q:
        V = Q.pop(0)
        BFS.append(V)
        for i in sorted(stack[V]):
            if visited_bfs[i] == False:
                visited_bfs[i] = True
                Q.append(i)


N, M, V = map(int,input().split())
lst = [list(map(int, input().split()))for _ in range(M)]
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)
stack = [[] for _ in range(N + 1)]

DFS = []
BFS = []
for i in range(M):
    stack[lst[i][0]].append(lst[i][1])
    stack[lst[i][1]].append(lst[i][0])
dfs(V)
bfs(V)
print(*DFS)
print(*BFS)