#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Rosalind 13 

def NumberToSymbol(number):
    if number == 0:
        return 'A'
    elif number == 1:
        return 'C'
    elif number == 2:
        return 'G'
    elif number == 3:
        return 'T'


def NumberToPattern(index, k):
    if k == 1:
        # return the symbol for last index
        return NumberToSymbol(index)
    
    # quotient
    prefixIndex = index // 4
    
    # remainder
    remainder = index % 4     
    
    PrefixPattern = NumberToPattern(prefixIndex, k - 1)
    
    symbol = NumberToSymbol(remainder)
    
    return PrefixPattern + symbol


# print it out
print(NumberToPattern(5702, 9))   

