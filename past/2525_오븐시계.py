# now_time = list(map(int, input().split()))
# hour = now_time[0]
# minute = now_time[1]
# plus_time = int(input())
#
# finish_minute = minute + plus_time
# i = 0
# if finish_minute > 60:
#     while finish_minute - 60:
#         i += 1
#         if finish_minute == 60:
#             finish_minute = 0
#         elif finish_minute < 60:
#             break
#
# finish_hour = hour + i
# if finish_hour > 24:
#     finish_hour -= 24
#
# print(f'{finish_hour} {finish_minute}')
now_time = list(map(int, input().split()))
hour = now_time[0]
minute = now_time[1]
plus_time = int(input())

finish_minute = minute + plus_time

if finish_minute >= 60:
    hour += finish_minute // 60
    finish_minute %= 60

if hour >= 24:
    hour %= 24

print(f'{hour} {finish_minute}')