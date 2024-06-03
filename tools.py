"""
Version: 1.0.0
Author: wuhaodes@qq.com
This is a tools module.
"""


def is_leap_year(year):
    """
    Check if a year is a leap year.
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")