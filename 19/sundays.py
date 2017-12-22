import datetime

SUNDAY = 6
total = 0
for year in range(1901, 2000 + 1):
    for month in range(1, 12 + 1):
        if datetime.date(year, month, 1).weekday() == SUNDAY:
            total += 1
print(total)
