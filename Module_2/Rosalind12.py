#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def SymbolToNumber(symbol):
    if symbol == "A":
        return 0
    elif symbol == "C":
        return 1
    elif symbol == "G":
        return 2
    elif symbol == "T":
        return 3
    else:
        return "Error"
     
def PatternToNumber(Pattern): 
    if Pattern == "":  
        return 0
    else:
        symbol = Pattern[-1]  # last symbol in pattern
        prefix = Pattern[:-1]  # all except the last symbol 
        return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)


pattern = "ATTGGGCTAAGGACTTTGCGCGCGGTTGC"
print(PatternToNumber(pattern))
    