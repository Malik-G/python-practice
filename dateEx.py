import datetime
#from datetime import datetime, timedelta

'''myDate = datetime.date(2017, 1, 10)

print(myDate.year)
print(myDate.month)
print(myDate.day)
print(datetime.datetime.today())'''

userBday = datetime.date(1993, 4, 30)
thisDay = datetime.date.today()
daysOld = thisDay - userBday
print (daysOld)
