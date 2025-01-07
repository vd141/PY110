import datetime

def friday_the_13ths(year):
    '''
    return number of friday the 13ths in a given year. assume the year is greater
    than 1792, which is when the UK adopted the gregorian calendar
    '''

    fridays = 0

    for month in range(1, 13):
        if datetime.date(year, month, 13).weekday() == 4:
            fridays += 1
    
    return fridays

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True