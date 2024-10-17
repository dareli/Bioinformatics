#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from All_Functions import pattern_count

# pattern method

# Text = "ATTGGTCGGGAGCGTGTTTTTTAGCTGCTACGGATGAGCGTGTTGTATGGAGAGCGTGTTATTGGTCGGCTACGGATGAGCGTGTTCTACGGATGAGCGTGTTGTATGGATTTTAGCTGTTTTAGCTGTTTTAGCTGGAGCGTGTTGAGCGTGTTTTTTAGCTGGTATGGAGTATGGATTTTAGCTGATTGGTCGGGTATGGACTACGGATCTACGGATGAGCGTGTTGTATGGAATTGGTCGGCTACGGATTTTTAGCTGGAGCGTGTTCTACGGATGAGCGTGTTTTTTAGCTGCTACGGATTTTTAGCTGATTGGTCGGCTACGGATATTGGTCGGTTTTAGCTGGTATGGACTACGGATTTTTAGCTGTTTTAGCTGGAGCGTGTTTTTTAGCTGGAGCGTGTTGTATGGACTACGGATGTATGGACTACGGATCTACGGATTTTTAGCTGGTATGGAATTGGTCGGTTTTAGCTGATTGGTCGGATTGGTCGGCTACGGATCTACGGATGTATGGAGAGCGTGTTTTTTAGCTGGTATGGAGTATGGAGTATGGAGAGCGTGTTCTACGGATATTGGTCGGCTACGGATGAGCGTGTTGAGCGTGTTATTGGTCGGGAGCGTGTTGAGCGTGTTTTTTAGCTGGTATGGATTTTAGCTGTTTTAGCTGGTATGGAATTGGTCGGATTGGTCGGATTGGTCGGTTTTAGCTGGTATGGACTACGGATGAGCGTGTTGTATGGACTACGGATGTATGGACTACGGATTTTTAGCTGGTATGGAATTGGTCGGGAGCGTGTTGTATGGACTACGGATTTTTAGCTGATTGGTCGGCTACGGATTTTTAGCTGCTACGGATGTATGGACTACGGATTTTTAGCTG"
# k = 14

#def FrequentWords(Text, k):
    #FrequentPatterns = set()  # to store the frequent k-mers
    #Count = [0] * (len(Text) - k + 1)  # count for ea. k-mer
    
    #for i in range(len(Text) - k + 1): # 
        #Pattern = Text[i:i+k]  # extract the pattern
        #Count[i] = pattern_count(Text, Pattern)  # count occurances of the k-mer
    
    #maxCount = max(Count)
    
    #for i in range(len(Text) - k + 1):     #find all k-mers w/ max count
        #if Count[i] == maxCount:
            #FrequentPatterns.add(Text[i:i+k])  # add k-mer to the set
    
    #return FrequentPatterns


# call the function & print the output
#result = FrequentWords(Text, k)
#print(" ".join(result)) 

# dictionary method 

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4

def frequent_kmers(text, k):
    #blank dictionary 
    kmer_counts = {}
    
    # Step 2: Loop through the DNA string to extract k-mers
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1
        else:
            kmer_counts[kmer] = 1
    
    #empty list to hold the most frequent k-mers
    list_of_keys = []
    
    max_count = max(kmer_counts.values())
    
    #loop over dictionary for k-mers w/ the max counts
    for kmer, count in kmer_counts.items():
        if count == max_count:
            list_of_keys.append(kmer)

    return list_of_keys

result = frequent_kmers(text, k)
print(" ".join(result))  




