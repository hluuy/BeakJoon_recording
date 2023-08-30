while True:
    A, B = map(int, input().split())
    if A + B == 0:
        break
    elif A - B > 0:
        print('Yes')
    elif A - B <= 0:
        print('No')