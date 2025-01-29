import datetime

def friday_the_13ths(year):
    '''
    takes a year as an argument
    returns the number of F13ths in that year
    year is greater than 1752
    assume the same calendar will remain in use for the forseeable future

    use the datetime.date functino to determine whether the 13th of a given
    month falls on a Friday

    the datetime.date(yyyy, mm, dd).weekday() function returns the day of the
    week as a number between 0 and 6 (inclusive)
        - friday is 4

    loop through the mm of the given year with the day set as 13. if the day is
    4, add 1 to the friday count
    '''

    count = 0

    for mm in range(1, 13):
        if datetime.date(year, mm, 13).weekday() == 4:
            count += 1
    
    return count



print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
