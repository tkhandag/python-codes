import datetime
date_entry = input('Enter a date in MM-DD-YYYY format')
month,day,year = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
print(date1)
day=datetime.datetime.strptime(date1, '%m %d %Y').strftime('%a')
print(day)