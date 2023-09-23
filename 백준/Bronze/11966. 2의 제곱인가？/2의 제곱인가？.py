N = int(input())
lst = [2**i for i in range(31)]

if N in lst:
    print(1)
else:
    print(0)