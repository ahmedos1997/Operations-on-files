# group
# يقوم هذا التابع بتقسيم الجملة الى اقسام حسب رغبة المستخدم تابع المثال التالي
import re

phone = '415-555-1234'
search = re.search(r'(\d{3})-(\d{3})-(\d{4})',phone)
print(search.group())
print(search.group(0))
print(search.group(1))
print(search.group(2))
print('------------------------------------------------------')

date = '22-03-2023'
search =re.search (r'(\d{2})-(\d{2})-(\d{4})',date)
day = search.group(1)
month = search.group(2)
year = search.group(3)
all = search.group()
print(f'the day is {day}: and the month is {month} : and the year is {year} ')
print(search.groups())