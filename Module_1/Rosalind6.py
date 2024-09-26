#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open ("/Users/darleneeligado/.spyder-py3/R6.txt", "r") as data:
    dna = data.read()
 
# function to count nucleotides   
def dna_counts(dna):
    a = dna.count('A')
    c = dna.count('C')
    g = dna.count('G')
    t = dna.count('T')
    
    print(a, c, g, t)
 
# call function    
dna_counts(dna)