import requests
url = "http://universities.hipolabs.com/search?country=India"
r = requests.get(url)
print(r.text)

# pip install requests

# pip install pillow

from math import sqrt

# from datetime import datetime, timedelta
#
# now = datetime.now()
# print(now)
#
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
#
# d1 = datetime(2020, 1, 1, 0, 0, 0)
#
# print(d1 < now)
# print(now < d1)
#
# diff = timedelta(days=1, hours=1)
# d2 = d1 + diff
# print(d2)
#
# d3 = datetime(2025, 8, 1, 0, 0, 0)
# diff2 = d3 - d1
# print(diff2)
#
# print(d3)
# print(f'{d3:%y年%m月%d日 %H时%M分%S秒}')
#
# d4 = datetime.strptime("25年08月01日 00时00分00秒", "%y年%m月%d日 %H时%M分%S秒")
# print(d4)

from datetime import date, timedelta

start_date =date(2000, 1, 1)
days_to_monday = 7 - start_date.weekday()
first_monday = start_date + timedelta(days_to_monday)
print(first_monday)

d =  date(2023, 1, 2)
print(f"{d:%b. %-d, %Y}")
print(f"{d:%B.} {d.day}, {d:%Y}, {d:%A}")
