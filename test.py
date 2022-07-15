def numberreverse(number: str) -> str:
    '''
    Reverse a number and return it as a string.
    :param number: number to reverse
    :return reversed_number: reversed number
    '''
    return ' '.join(number.split()[::-1])

print(numberreverse("10 20 30 40`50"))
