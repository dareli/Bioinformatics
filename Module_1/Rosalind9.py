#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Bio.SeqIO import parse
from Bio.SeqUtils import GC

max_gc = 0 

for seq_record in parse("/Users/darleneeligado/.spyder-py3/R9.txt", "fasta"):
    
    if GC(seq_record.seq)  > max_gc:
        max_gc = GC(seq_record.seq)
        max_recodID = seq_record.id

print(max_recodID, max_gc, sep = "\n")  