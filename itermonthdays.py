import calendar
cal=calendar.Calendar(firstweekday=0)
for x in cal.itermonthdates(2018,3):
    print(x)