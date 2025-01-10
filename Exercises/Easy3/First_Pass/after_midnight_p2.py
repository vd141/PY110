HOURS_IN_A_DAY = 24
MINUTES_IN_AN_HOUR = 60
MINUTES_IN_A_DAY = HOURS_IN_A_DAY * MINUTES_IN_AN_HOUR

def after_midnight(time_):
    time_split = time_.split(':')
    hours = int(time_split[0])
    minutes = int(time_split[1])

    minutes_after_midnight = (hours * MINUTES_IN_AN_HOUR) + minutes

    while minutes_after_midnight >= MINUTES_IN_A_DAY:
        minutes_after_midnight -= MINUTES_IN_A_DAY
    
    return minutes_after_midnight

def before_midnight(time_):
    '''
    given a time, calculate the number of minutes before midnight that time is

    calculate the minutes after midnight the time is, then subtract that number
    from the number of minutes in a day to get the number of minutes before
    midnight
    '''
    time_split = time_.split(':')
    hours = int(time_split[0])
    minutes = int(time_split[1])
    
    minutes_before_midnight = (MINUTES_IN_A_DAY - (hours * MINUTES_IN_AN_HOUR)
    - minutes)

    while minutes_before_midnight >= MINUTES_IN_A_DAY:
        minutes_before_midnight -= MINUTES_IN_A_DAY

    return minutes_before_midnight

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True