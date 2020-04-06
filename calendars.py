import calendar

# text calendar
# c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2020, 2, 0, 0)
# print(st)

# Html calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st =  hc.formatmonth(2020, 4)
# print(st)

# iterate over month dates
# for i in c.itermonthdates(2020,8):
#     print(i)

# iterate over month names
# for name in calendar.month_name:
#     print(name)

# iterate over day names
# for day in calendar.day_name:
    # print(day)

print('team meetings will be on')
for m in range(1,13):
    cal = calendar.monthcalendar(2020, m)
    weekone = cal[0]
    weektwo =  cal[1]

    if weekone[calendar.FRIDAY != 0]:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    print("%10s %2d" % (calendar.month_name[m], meetday))