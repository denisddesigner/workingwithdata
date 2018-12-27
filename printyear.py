import calendar
year = int(input("Enter the year to display: "))
print(calendar.prcal(year))


cal = calendar.TextCalendar(calendar.SUNDAY)
for i in cal.itermonthdays(2018,6):
    print(i)


for name in calendar.month_name:
    print(name)
