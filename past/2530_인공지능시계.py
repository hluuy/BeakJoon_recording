now_time = list(map(int, input().split()))
hour = now_time[0]
minute = now_time[1]
second = now_time[2]
plus_second = int(input())

finish_second = second + plus_second

if plus_second >= 60:
    minute += finish_second // 60
    finish_second %= 60

if minute >= 60:
    hour += minute // 60
    minute %= 60

if hour >= 24:
    hour %= 24

print(f'{hour} {minute} {finish_second}')