K = int(input())
num = [input() for _ in range(K)]
stack = []
result = 0
for i in num:
    if i == '0':
        stack.pop()
    else:
        stack.append(i)
for i in stack:
    result += int(i)
if not stack:
    print(0)
else:
    print(result)
