# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.

days_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]

# Account for leap days. 

def is_leap_year(year1):
    year=True
    if year1 % 4 !=0:
        year=False
    elif year1 % 100 !=0:
        year=True
    elif year1 % 400 !=0:
        year=False
    else: year=True
    return year
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
def days_in_month(year, month):
    days=0
    if is_leap_year(year) and month == 2:
        days += 29
    else: days += days_of_months[month - 1]
    return days
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days=total_days(year1, month1, year2, month2)
    return days-day1+day2
    
##tie in defs

def total_days (year1, month1, year2, month2):
    days=0
    while year1<year2 or month1<month2:
        days += days_in_month(year1, month1)
        month1 += 1
        if month1 == 13:
            year1 += 1
            month1 = 1
    return days

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
