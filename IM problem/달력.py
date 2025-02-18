def which_day(a, b):
    cnt = b-1
    for i in range(a):
        cnt += days_in_month[i]

    return day[cnt % 7]


day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(which_day(5, 24))