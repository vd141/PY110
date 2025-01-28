def friday_the_13ths(year):
    '''
    takes a year as an argument
    returns the number of F13ths in that year
    year is greater than 1752
    assume the same calendar will remain in use for the forseeable future

    use the datetime.date functino to determine whether the 13th of a given
    month falls on a Friday

    
    '''




print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True