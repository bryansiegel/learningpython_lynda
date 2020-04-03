def is_leap(year):
    leap = False

    year = year / 4

    if year / 4 and year % 2 == 0:
        leap = True
    elif year / 100 and year % 2 !=0:
        leap = False
    elif year % 400:
        leap = True
    return leap


year = int(input())
print(is_leap(year))
