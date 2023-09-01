STR = input()
REVERSE = ''
for i in list(reversed(STR)):
    REVERSE += i
if STR == REVERSE:
    print(1)
else:
    print(0)