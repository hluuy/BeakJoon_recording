a = int(input())
b = input()

c = list(map(int, b))

print(a * c[-1])
print(a * c[-2])
print(a * c[-3])
print(a * int(b))