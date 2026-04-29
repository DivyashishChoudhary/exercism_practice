def leap_year(year):
    remainder_by_four = year%4
    remiander_by_hundred = year%100
    remainder_by_fourhundred = year%400
    if  remainder_by_four == 0:
        if remiander_by_hundred == 0:
            if remainder_by_fourhundred == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    