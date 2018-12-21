days = int(input())

activities = [int(x) for x in input().split()]

free_days = 0
last_activity = 0
both_count = 0
for activity in activities:
    if activity == 3:
        both_count += 1
    else:
        if activity == 0:
            free_days += 1
            last_activity = 0
        elif last_activity != 0 and \
             (both_count % 2 == 0 and last_activity == activity or \
             both_count % 2 != 0 and last_activity != activity):
            free_days += 1
            last_activity = 0
        else:
            last_activity = activity
        both_count = 0

print(free_days)