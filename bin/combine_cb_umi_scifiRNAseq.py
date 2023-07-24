# Script for combining the 10x cellbarcode and UMI into one fastq file for further processing with starsolo
# It's slightly modified script from the ISSAACseq github pipeline

import sys
import gzip

umi = gzip.open(sys.argv[1], mode='rt') # read the fastq with UMI
cellbarcode = gzip.open(sys.argv[2], mode='rt') # read the fastq with cellbarcode

for UMIname, UMIsequence, _, UMIquality, CBname, CBsequence, _, CBquality in zip(umi, umi, umi, umi, cellbarcode, cellbarcode, cellbarcode, cellbarcode): #Read in the fastq files by four lines at a time, read in both fastqs at the same time
    n1 = UMIname.split(' ')[0] # don't take the read number into account, just the read name
    n2 = CBname.split(' ')[0]
    assert n1 == n2 # check if first line (readname) is the same 
    print(UMIname.strip()) # print the name of UMIread
    print(CBsequence[:16] + UMIsequence[:8]) # take the first 16 bases (all) of CB fastq - read 1 fastq.gz file and the first 8 bases of the UMI fastq - index1 fastq.gz file
    print('+')
    print(CBquality[:16] + UMIquality[:8])
