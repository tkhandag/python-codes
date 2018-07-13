import calendar
cal=calendar.Calendar(firstweekday=0)
for x in cal.itermonthdays2(2018,3):
    print(x)