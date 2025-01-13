MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
MINUTES_IN_DAY = MINUTES_IN_HOUR * HOURS_IN_DAY

def after_midnight(time_str):
    '''
    return minutes after midnight given a time_str

    convert tiem string to minutes after midnight. if the number of minutes
    after midnight is greater than or equal to number of minutes in a day,
    subtract number of minutes in day until number is between 0 and number of
    minutes in a day

    return number
    '''

    time_split = time_str.split(':')

    minutes_after_midnight = int(time_split[0]) * MINUTES_IN_HOUR + int(time_split[1])

    while minutes_after_midnight >= MINUTES_IN_DAY:
        minutes_after_midnight -= MINUTES_IN_DAY

    return minutes_after_midnight


def before_midnight(time_str):
    '''
    return minutes before midnight given a time_str

    convert time string to minutes after midnight. then subtract from
    number of minutes in a day
    '''
    
    return (MINUTES_IN_DAY - after_midnight(time_str) if after_midnight(time_str) != 0 else 
            after_midnight(time_str))

    


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True