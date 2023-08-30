# T = int(input())
# for t in range(1, T + 1):
#     A, B = map(int, input().split())
#     lst_a = []
#     lst_b = []
#     result = []
#     for i in range(1, 45001):
#         lst_a.append(A * i)
#         lst_b.append(B * i)
#     for i in range(len(lst_a)):
#         if lst_a[i] in lst_b:
#             result.append(lst_a[i])
#     result.sort()
#     print(result[0])
T = int(input())
for t in range(1, T + 1):
    A, B = map(int, input().split())
    AA, BB = A, B

    while BB != 0:
        AA = AA % BB
        AA, BB = BB, AA

    result = A * B // AA
    print(result)