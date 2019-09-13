def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            pass
        else:
            leap = True
    else:
        pass

    return leap


year = int(input())