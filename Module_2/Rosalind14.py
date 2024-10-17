#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Rosalind 14

# from Rosalind 12 (PatternToNumber)
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
    
def ComputingFrequencies(Text, k):
    FrequencyArray = [0] * (4 ** k)
    
    for i in range(len(Text) - k + 1): 
        Pattern = Text[i:i+k]
        j = PatternToNumber(Pattern)  # k-mer to a number 
        FrequencyArray[j] += 1  # increment freq. of k-mer
    
    return FrequencyArray


Text = "TTTTAACTGTAATCGGTTGCAAATACGACGAGTGCAAAGAGAACCATAGCGTCAGCTCGTGGCAGTGCCGCGCGTGCAAAGCTCCTTTCTATTGCTTCAAGATTGGTCGGCGCGGCATTCATAGACCGGACGGGAGCCCATCTGTCTAAATTTCTGAAAATCAGGAAACAGGAACTGCTCCCTGCTTGAGTGTAGAAATACCCGTCATACGCCGAGGGTGGCCAACCAATTGAAGGGCGCTGGCATCAACTCGGGGCGCTGTTCGCTTTGGGGTTTGAAAAATGTCCCTACCCGAAGGCAGAGGATCTGCCCACGAATAGTCTCGAGCCAGACGCCAACACCCTTATGAAACTTAAAACAAGTACCCCAGCCAACGCGGGCCCAATCTGTTGGAATCGCTAAGGCTGCATTGACCTTAATACCAGTGTCCTCCTCCAAATCTAAATCTCTCCTTCAAATTTCAGCCGCCTACGCTAAGTGATGCGGCAAGAATTCTAGGTGTTGGCCGGAAGGCTTAAGCTTACGGTGACACGCATAATTATAGTATTACCTTATTAGATCCGCCGTGACCACCGTCAAGTTACAAGTTACGCTTAATGGGCAGATCTTAACTGGTAATTCATACGCCGAGCGTTTCTCTTCCCTGCTAAGTTGCGCGGCGAAGATTTTTAGCGCTTGAACTTGCACCACTGCTCCGGTTAGTGGCAGACGAGGCGCC"
k = 7 

# print & space integers
result = ComputingFrequencies(Text, k)
print(" ".join(map(str, result))) 