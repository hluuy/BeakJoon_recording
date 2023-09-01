T = int(input())
max_money = 0
for t in range(T):
    lst = list(map(int, input().split()))
    blank = [[]for _ in range(7)]
    max_count = 0
    max_num = 0
    money = 0
    for i in lst:
        blank[i].append(1)
    for i in range(7):
        if len(blank[i]) > max_count:
            max_count = len(blank[i])
            max_num = i
    if max_count == 1:
        money = (max(lst) * 100)
    elif max_count == 2:
        money = (max_num * 100 + 1000)
    else:
        money = (max_num * 1000 + 10000)

    if money > max_money:
        max_money = money
print(max_money)