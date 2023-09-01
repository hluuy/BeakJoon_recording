N = int(input())
opinion = []
for i in range(N):
    opinion.append(int(input()))
if opinion.count(1) > opinion.count(0):
    print('Junhee is cute!')
elif opinion.count(1) < opinion.count(0):
    print('Junhee is not cute!')