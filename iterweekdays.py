import calendar
cal=calendar.Calendar(firstweekday=0)
for x in cal.iterweekdays():
    print(x)