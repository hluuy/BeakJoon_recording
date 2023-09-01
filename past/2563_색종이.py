T = int(input())
background = [[0] * 100 for _ in range(100)]
for t in range(T):
    N, M = map(int, input().split())
    x1 = N
    y1 = M
    x2 = N+10
    y2 = M+10
    sum_v = 0
    for i in range(x1, x2):
        for j in range(y1, y2):
            if 0<= i < 100 and 0<= j < 100:
                background[i][j] = 1
    for i in range(100):
        for j in range(100):
            if background[i][j] == 1:
                sum_v += 1
print(sum_v)

#     for i in range(100):
#         for j in range(100):
#             x1 = N
#             y1 = M
#             x2 = N+10
#             y2 = M+10
#             for p in range(x1, x2):
#                 for q in range(y1, y2):
#                     if 0<= p < 100 and 0 <= q < 100:
#                         background[p][q] += 1
# # for i in range(100):
# #     for j in range(100):
#             if background[i][j] > 1:
#                 background[i][j] = 1
#             if background[i][j] == 1:
#                 sum_v += 1


    #                 if 0 <= N < 89 and 0 <= M < 89:
    #                     background[p][q] = 1
    #         if background[i][j] > 1:
    #             background = 1
    # for i in range(10):
    #     for j in range(10):
    #         sum_v += background[i][j]


    # for i in range(N, N+10):
    #     for j in range(M, M + 10):
    #         if 0<= i < 100 and 0<= j < 100:
    #             background[i][j] = 1
    #
    # for i in range(100):
    #     for j in range(100):
    #         sum_v += background[i][j]
    # print(sum_v)