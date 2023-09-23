import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    command, *args = input().split()
    if command == 'add':
        S.add(int(args[0]))
    elif command == 'remove':
        S.discard(int(args[0]))
    elif command == 'check':
        if int(args[0]) in S:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if int(args[0]) in S:
            S.discard(int(args[0]))
        else:
            S.add(int(args[0]))
    elif command == 'all':
        S.update(range(1, 21))
    elif command == 'empty':
        S.clear()
