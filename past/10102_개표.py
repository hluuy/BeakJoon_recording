N = int(input())
vote = input()
vote_A = []
vote_B = []
for choose in vote:
    if choose == 'A':
        vote_A.append(choose)
    else:
        vote_B.append(choose)
if len(vote_A) > len(vote_B):
    print('A')
elif len(vote_A) < len(vote_B):
    print('B')
else:
    print('Tie')