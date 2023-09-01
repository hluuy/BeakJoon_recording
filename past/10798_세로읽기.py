STR = [list(input()) for _ in range(5)]
result = ''
max_len = max(len(word) for word in STR)
for i in range(max_len):
# for i in range(len(STR[0])):
    for j in range(5):
        if i < len(STR[j]):
            result += STR[j][i]
print(result)