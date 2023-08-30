price, num_snack, money = map(int, input().split())
wanted = price * num_snack - money
if wanted < 0:
    print(0)
else:
    print(wanted)