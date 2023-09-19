import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True
    for i in MAP[v]:
        if visited[i] == 0:
            dfs(i)

N, M = map(int, input().split())
MAP = [[] for _ in range(N + 1)]
count = 0
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    MAP[i].append(j)
    MAP[j].append(i)

visited = [False] * (N + 1)
for i in range(1, N + 1):
    if visited[i] == 0:
        dfs(i)
        count += 1

print(count)