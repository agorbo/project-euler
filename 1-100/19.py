import datetime

current_date = datetime.date(1901, 1, 1)
final_date = datetime.date(2001, 1, 1)

sundays_count = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if datetime.date(year, month, 1).weekday() == 6:
            sundays_count += 1

print(sundays_count)
