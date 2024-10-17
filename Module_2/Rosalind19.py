#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Rosalind 19, Generate the d-Neighborhood of a String

def neighbors_d(pattern):
    nucleotides = ['A', 'C', 'G', 'T']
    neighbors = [] # list to hold neighbors 
    
    for i in range(len(pattern)): # all possible substitution at ea. position 
        for substitution in nucleotides:
            if pattern[i] != substitution:
                new_pattern = pattern[:i] + substitution + pattern[i+1:] # new pattern w/ the substitution
                neighbors.append(new_pattern)
                
                
    return neighbors


def neighborhood(pattern, d):
    master_list = neighbors_d(pattern)
    
    if d == 1: 
        return master_list
    
    for _ in range(d -1):
        temp_list = [] # temporary list to hold new neighbors 
        
        for current_pattern in master_list:
            temp_list.extend(neighbors_d(current_pattern)) # neighbors of current_pattern
            
        master_list.extend(temp_list)
    
    # return neighbor list to a set & then back to list
    return list((set(master_list)))


pattern = "CCGTGGAGCCA"
d = 2 

result = neighborhood(pattern, d)
for neighbor in sorted(result):
    print(neighbor)  
    
    
    