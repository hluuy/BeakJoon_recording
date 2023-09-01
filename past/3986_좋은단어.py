N = int(input())
cnt = 0
for _ in range(N):
    arr = input()
    lst = []

    for i in arr:
        lst.append(i)
        if len(lst) > 1:
            if lst[-1] == lst[-2]:
                lst.pop()
                lst.pop()
    if len(lst) == 0:
        cnt += 1

print(cnt)

# arr = [list(input())for _ in range(N)]
# lst = []
# cnt = 0
# for i in arr:
#     print(i)
    # if i in ['A','B']:
    #     lst.append(i)
    #         if i > 1:
    #             if arr[i] == arr[i-1]:
    #                 arr.pop(lst[i])
    #                 lst.pop(lst[i-1])
    #                 cnt += 1
#
# print(cnt)