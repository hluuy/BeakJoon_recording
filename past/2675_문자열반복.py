T = int(input())
for t in range(1, T + 1):
    R, STR = input().split()
    result = ''
    for item in STR:
        result += int(R)*item
    print(result)