N, M = map(int, input().split())
MAP1 = [list(map(int, input().split()))for _ in range(N)]
MAP2 = [list(map(int, input().split()))for _ in range(N)]
MAP3 = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        a = MAP1[i][j]
        b = MAP2[i][j]
        MAP3[i][j] = a + b
for i in MAP3:
    print(*i)
