#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Rosalind 23, Frequent Words with Mismatches and Reverse Complements Problem

from Bio.Seq import Seq

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

'''
# rosalind 21 code
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
'''

# from rosalind 22
def reverse_complement(dna_string): 
    dna_seq = Seq(dna_string)
    return str(dna_seq.reverse_complement())

# integrate 22 in 21 for rosalind 23
def mismatch_reverse_complement(text, k, d):
    frequency_dictionary = {}  # to store frequencies for k-mers and their neighbors
    
    for i in range(len(text) - k + 1):  # go over all k-mers in the text
        kmer = text[i:i+k]
        neighborhood_kmers = neighborhood(kmer, d) # neighbors w/ up to d mismatches
        
        reverse_kmer = reverse_complement(kmer) # reverse complement neighborhood
        neighborhood_kmers_rc = neighborhood(reverse_kmer, d) 
        
        # combine neighborhoods of the k-mer & its rcs
        all_neighbors = set(neighborhood_kmers).union(set(neighborhood_kmers_rc))
        
        # count occurrences for each neighbor (k-mers & rcs)
        for neighbor in all_neighbors:
            
            if neighbor not in frequency_dictionary:
                # count the k-mer & its rc
                count_neighbor = approx_pattern_count(neighbor, text, d)
                count_rc_neighbor = approx_pattern_count(reverse_complement(neighbor), text, d)
                # store the total count in the dictionary
                frequency_dictionary[neighbor] = count_neighbor + count_rc_neighbor
    
    # max frequency
    max_count = max(frequency_dictionary.values())
    
    #all k-mers w/ the maxfrequency
    most_frequent_kmers = [kmer for kmer, count in frequency_dictionary.items() if count == max_count]
    
    return most_frequent_kmers


text = "AGAAAGCCAAGTGTGGTAATAAGACAAATCGGAATAAGACAGAAAGCCAGGGGCAAGGGGCAAAATAAGACAATAAGACAGTGTGGTAGTGTGGTAGAAAGCCAAGAAAGCCAAGTGTGGTAGAAAGCCAAGTGTGGTAGAAAGCCAAGAAAGCCAAATAAGACAATAAGACAAATCGGAGAAAGCCAAAATCGGAATAAGACAGTGTGGTAGAAAGCCAAATAAGACGGGGCAAAGTGTGGTAGAAAGCCAGGGGCAAAGTGTGGTGGGGCAAAGTGTGGTAGTGTGGTAGTGTGGTAGAAAGCCAAAATCGGAGAAAGCCAAGTGTGGTAGAAAGCCAAAATCGGAGTGTGGTAATAAGACAGAAAGCCAGGGGCAAGGGGCAAGGGGCAAAGTGTGGTAGTGTGGTGGGGCAAAATAAGACAATAAGACAGTGTGGTAGAAAGCCAGGGGCAAAATAAGACAAATCGGGGGGCAAAGTGTGGTAAATCGGAAATCGGAATAAGACGGGGCAAGGGGCAAAGAAAGCCAAGTGTGGTAATAAGACAAATCGGGGGGCAAAGTGTGGTAAATCGGAATAAGACAGTGTGGTGGGGCAAAAATCGGAATAAGACAGAAAGCCAAATAAGACAATAAGACAGAAAGCCAAGAAAGCCAGGGGCAAAGTGTGGTAAATCGGAGTGTGGTAGAAAGCCAAGTGTGGTAAATCGGAATAAGACAATAAGACAAATCGGAGTGTGGTAATAAGACAATAAGACAGTGTGGTGGGGCAAAGAAAGCCAAGAAAGCCAAAATCGGGGGGCAAAAATCGGGGGGCAA"
k = 6
d = 3

# Get the result
result = mismatch_reverse_complement(text, k, d)
print(*result)  






