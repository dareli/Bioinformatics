#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Rosalind 21, Frequent Words with Mismatches Problem 

# from roslind 18
def hamming_distance(sequence1, sequence2):
    distance = 0
    for i in range(len(sequence1)):
        if sequence1[i] != sequence2[i]:  # check if positions match
            distance += 1
    return distance

# from rosalind 19
def neighbors_d(pattern):
    nucleotides = ['A', 'C', 'G', 'T']
    neighbors = [] # list to hold neighbors 
    
    for i in range(len(pattern)): # all possible substitution at ea. position 
        for substitution in nucleotides:
            if pattern[i] != substitution:
                new_pattern = pattern[:i] + substitution + pattern[i+1:] # new pattern w/ the substitution
                neighbors.append(new_pattern)
                
                
    return neighbors

# from rosalind 19
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

# from rosalind 20, modified to count
def approx_pattern_count(pattern, text, d):
    count = 0
    k = len(pattern)
    for i in range(len(text) - k + 1):
        window = text[i:i+k]
        if hamming_distance(pattern, window) <= d:
            count += 1
    return count

def frequent_words_mismatches(text, k, d):
    frequency_dictionary = {}  # to store frequencies & their neighbors
    
    for i in range(len(text) - k + 1): # to go over all k-mers
        kmer = text[i:i+k] 
        neighborhood_kmers = neighborhood(kmer, d)  # neighbors w/ up to d mismatches
        
        
        for neighbor in neighborhood_kmers:
            if neighbor not in frequency_dictionary:
                frequency_dictionary[neighbor] = approx_pattern_count(neighbor, text, d)
    
    # max  frequency
    max_count = max(frequency_dictionary.values())
    
    # all k-mer w/ max frequency
    most_frequent_kmers = [kmer for kmer, count in frequency_dictionary.items() if count == max_count]
    
    return most_frequent_kmers

text = "CGTTTGCTACGTTTGCTACGTTTGCTACGTTTGCTAGATCCCTCCACGTTTGCTATTGGCTCGGGGAGAGTCAGGAGAGTCAGGTTACCTCGTTACCTCGTTACCTCGATCCCTCCAGAGAGTCAGGTTACCTCGTTACCTCGATCCCTCCAGTTACCTCTTGGCTCGGGGTTACCTCGAGAGTCAGCGTTTGCTACGTTTGCTAGAGAGTCAGCGTTTGCTAGTTACCTCCGTTTGCTATTGGCTCGGGGATCCCTCCAGATCCCTCCAGATCCCTCCAGAGAGTCAGCGTTTGCTAGTTACCTCGAGAGTCAGCGTTTGCTAGATCCCTCCATTGGCTCGGGGTTACCTCGTTACCTCGTTACCTCTTGGCTCGGGGATCCCTCCACGTTTGCTATTGGCTCGGGCGTTTGCTAGATCCCTCCAGTTACCTCGAGAGTCAGGTTACCTCTTGGCTCGGGGTTACCTCCGTTTGCTAGATCCCTCCAGATCCCTCCAGTTACCTCTTGGCTCGGGTTGGCTCGGGGATCCCTCCAGAGAGTCAGTTGGCTCGGGTTGGCTCGGGCGTTTGCTAGTTACCTCCGTTTGCTAGATCCCTCCAGAGAGTCAGGATCCCTCCAGTTACCTCGTTACCTCGTTACCTCTTGGCTCGGGTTGGCTCGGGGAGAGTCAGTTGGCTCGGGTTGGCTCGGGCGTTTGCTAGAGAGTCAGGTTACCTCTTGGCTCGGGGTTACCTCGATCCCTCCAGTTACCTCTTGGCTCGGGTTGGCTCGGGTTGGCTCGGGCGTTTGCTAGTTACCTCCGTTTGCTAGAGAGTCAGGTTACCTCGTTACCTCCGTTTGCTAGATCCCTCCAGATCCCTCCAGATCCCTCCATTGGCTCGGGTTGGCTCGGGGTTACCTCCGTTTGCTACGTTTGCTAGATCCCTCCACGTTTGCTATTGGCTCGGG"
k = 7
d = 2

result = frequent_words_mismatches(text, k, d)
print(*result)  
