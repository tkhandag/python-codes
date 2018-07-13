import datetime
t=datetime.datetime.strptime('January 11 ,2018', '%B %d, %Y').strftime('%A')
print(t)
