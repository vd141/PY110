def time_of_day(num):
    '''
    input is number of minutes before/after midnight

    return the 24 hour time (hh:mm) relative to midnight based on the input

    60 minutes in an hour. 24 hours in a day.

    num % 60 is the minute value

    num // 60 is the hour value

    use str.zfill() to fill hours and minutes
    '''

    if num >= 0:
        if num // 60 > 24:
            hour = str((num // 60) % 24)
        else:
            hour = str(num // 60)
        minutes = str(num % 60)
    else:
        pass
        # if the minutes are negative, find the minute value by subtracting
        # minutes from 60
        if (num // 60) < -24:
            hour = str((num // 60) % 24)
        else:
            hour = str(24 + (num // 60))
        minutes = str(num % 60)

    return f'{hour.zfill(2)}:{minutes.zfill(2)}'

