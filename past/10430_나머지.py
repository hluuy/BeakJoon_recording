a, b, c = map(int, input().split())
first_result = (a + b) % c
second_result = ((a % c) + (b % c)) % c
third_result = (a * b) % c
fourth_result = ((a % c) * (b % c)) % c
print(first_result)
print(second_result)
print(third_result)
print(fourth_result)