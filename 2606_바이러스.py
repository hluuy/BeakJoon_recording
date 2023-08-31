def dfs(v):
    global count
    visited[v] = True
    for i in stack[v]:
        if visited[i] == False:
            dfs(i)
            count += 1
    return count

V = int(input())
E = int(input())
lst = [list(map(int, input().split()))for _ in range(E)]
visited = [False] * (V + 1)
stack = [[]for _ in range(V + 1)]
count = 0
for i in range(E):
    stack[lst[i][0]].append(lst[i][1])
    stack[lst[i][1]].append(lst[i][0])
dfs(1)
print(count)