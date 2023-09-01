def bfs(V):
    Q = []
    Q.append(V)
    while Q:
        V = Q.pop(0)
        if V == K:
            return visited[V]
        for i in (V - 1, V + 1, 2 * V):
            if 0 <= i < 100001 and visited[i] == False:
                visited[i] = visited[V] + 1
                Q.append(i)


N, K = map(int, input().split())
visited = [False] * 100001
if N == K:
    print(0)
else:
    result = bfs(N)
    print(result)