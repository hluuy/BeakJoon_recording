lst = list(map(int, input().split()))
blank = [[] for _ in range(7)]
max_count = 0
max_num = 0
for i in lst:
    blank[i].append(1)
for i in range(7):
    if len(blank[i]) > max_count:
        max_count = len(blank[i])
        max_num = i
if max_count == 1:
    print(max(lst) * 100)
elif max_count == 2:
    print(max_num * 100 + 1000)
else:
    print(max_num * 1000 + 10000)