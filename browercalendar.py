import calendar
cal = open("/home/pi/Documents/cal.html", "w")
c = calendar.HTMLCalendar(calendar.SUNDAY)
cal.write(c.formatmonth(2018, 1))
cal.close()
