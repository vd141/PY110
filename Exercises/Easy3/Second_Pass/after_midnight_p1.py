MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
MINUTES_IN_DAY = MINUTES_IN_HOUR * HOURS_IN_DAY

def time_of_day(minutes):
    '''
    if the num of minutes is positive, the time is after midnight. if the num
    of minutes is negative, the time is before midnight

    takes a time using minute-based format and returns the time of day in 24-hr
    format (hh:mm). your function should work with any integer input
    
    calculate minutes in a day

    input minutes must be converted into the minute of the day (between 0 and
    total number of mintues in a day)

    from there, converted_time % 60 to get minutes

    converted_time // 24 to get hour
    '''

    while minutes > MINUTES_IN_DAY:
        minutes -= MINUTES_IN_DAY

    while minutes < 0:
        minutes += MINUTES_IN_DAY

    hour = str(minutes // MINUTES_IN_HOUR).zfill(2)
    minute = str(minutes % MINUTES_IN_HOUR).zfill(2)

    return f'{hour}:{minute}'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True