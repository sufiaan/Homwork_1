"""
Sufiaan Shaikh-1859029

CIS-2348-18349

Homework-1
"""

from datetime import date


def calculate_age(current_date, birth_date):
    today = current_date
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    return age


print("Birthday Calculator")
print('current Day')
current_month = int(input('Month: '))
current_day = int(input('Day: '))
current_year = int(input('Year: '))
print('Birthday')
birth_month = int(input('Month: '))
birth_day = int(input('Day: '))
birth_year = int(input('Year: '))
print("you are ", calculate_age(date(current_year, current_month, current_day), date(birth_year, birth_month, birth_day)), "years old.")
if current_day == birth_day and current_month == birth_month:
    print("Happy Birthday!")
