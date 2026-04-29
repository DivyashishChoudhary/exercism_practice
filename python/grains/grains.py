def square(number):
    if 1 <= number <= 64:
        return (2**(number-1))
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    sum = 0
    for n in range(1,65):
        sum = sum + 2**(n-1)
    return sum


