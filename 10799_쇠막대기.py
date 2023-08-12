pipe = input()
count = 0
ans = 0
for i in range(len(pipe)):
    if pipe[i] == '(':
        count += 1
    else:
        if pipe[i-1] != '(':
            count -= 1
            ans += 1
        else:
            count -= 1
            ans += count
print(ans)