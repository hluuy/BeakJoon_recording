N = int(input())
sum = 0
result = 0
for i in range(1, N + 1):
    sum += i
    result = i
    if sum > N:
        result -= 1
        break
print(result)