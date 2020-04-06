from datetime import date, time, datetime, timedelta

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
# print(now)

#one year form now
# print('one year from now is ' + str(now + timedelta(days=365)))

#multiple arguments
# print("In 2 days and 3 weeks will be " + str(now + timedelta(days=2, weeks=3)))

#format one week ago
# t = datetime.now() - timedelta(weeks=1)
# s = t.strftime('%A %B %d, %Y')
# print("one week ago was " + s)

#Calculate April fools day
today = date.today()
afd = date(today.year, 4, 1)
if(afd < today):
    print("aprils fool day happened by %d days ago" % ((today - afd).days))
    afd = afd.replace(year = today.year + 1)

time_to_afd = afd - today
print('it is just ', time_to_afd.days, 'days until april fools day')