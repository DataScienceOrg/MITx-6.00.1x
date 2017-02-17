# -*- coding: utf-8 -*-


def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    prevexp = 0
    exp = 0

    while True:
        prevexp = exp
        exp += 1       
        if base ** exp > num:
            if abs(num - base ** prevexp) > abs(base ** exp - num):
                return exp
            else:
                return prevexp
     

#closest_power(3,12) #returns 2
#closest_power(4,12) #returns 2
#closest_power(4,1) #returns 0

