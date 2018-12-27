import calendar
cal = open("/Users/denism/Downloads/cal.html", "w")
c = calendar.HTMLCalendar(calendar.SUNDAY)
cal.write(c.formatmonth(2018, 1))
cal.close()
