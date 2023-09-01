T = int(input())
for _ in range(T):
    PS = input()
    lst = []
    for i in PS:
        if i in '()':
            lst.append(i)
            if len(lst) > 1:
                if lst[-1] == ')' and lst[-2] == '(':
                    lst.pop()
                    lst.pop()

    if len(lst) > 0:
        print('NO')
    else:
        print('YES')
