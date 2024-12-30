DEGREE = "\u00B0"

def dms(flt):
    '''
    a function that takes a floating point number representing an angle between
    0 and 360 degrees and returns a string representing that angle in degrees,
    minutes, and seconds. 

    if the input is a whole number, minutes and seconds are 0

    if the input is a float, the minutes is determined by multiplying the decimal
    by 60, and the seconds is determined by multiplying the decimal of the minutes
    by 60

    use an f string to print the final string. insert the degrees, minutes, and
    seconds into the final string

    degrees are determined by subtracting the int(degrees) from float(degrees)
    '''

    degrees = int(flt)
    if abs(degrees) > 360:
        degrees = degrees % 360
    if -360 <= degrees < 0:
        degrees = degrees + 360
    minutes = (flt - int(flt)) * 60
    seconds = (minutes - int(minutes)) * 60

    str_degrees = str(degrees)
    str_minutes = str(int(minutes)).zfill(2)
    str_seconds = str(int(seconds)).zfill(2)

    return f'{str_degrees}{DEGREE}{str_minutes}\'{str_seconds}"'


# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"