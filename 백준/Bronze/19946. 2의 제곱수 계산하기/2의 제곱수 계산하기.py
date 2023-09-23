N = int(input())
K = 64

while (1):
    if(N % 2 == 1):
        break
    N //= 2
    K -= 1

print(K)