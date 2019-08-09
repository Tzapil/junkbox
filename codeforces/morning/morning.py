# 816A. Карен и утро

def diff_time(time1, time2):
    diff = 0
    if time2[0] >= time1[0]:
        diff += (time2[0] - time1[0]) * 60
    else:
        diff += ((24 - time1[0]) + time2[0]) * 60
    diff += time2[1] - time1[1]

    return diff

def is_palindrome(time):
    answer = True
    hours, minutes = ('{:02d}'.format(x) for x in time)

    for i in range(2):
        if hours[i] != minutes[1 - i]:
            answer = False
            break

    return answer

hours_s, minutes_s = [int(x) for x in input().split(':')]
hours, minutes = hours_s, minutes_s

while not is_palindrome((hours, minutes)):
    minutes_n = int(''.join(reversed('{:02d}'.format(hours))))
    if minutes_n < 60 and minutes_n >= minutes:
        minutes = minutes_n
        break

    hours = (hours + 1) % 24
    minutes = 0

print(diff_time((hours_s, minutes_s), (hours, minutes)))



