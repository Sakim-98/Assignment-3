import re 
import pandas as pd

def fastaReader(filename):
    """ Removes the fasta identifier line starting with '>' and returns only the DNA sequence as a string """
    
    genome = ''

    with open(filename, 'r') as f:  # Open the fasta file

        for line in f:

            if not line[0] == '>':  # ignore the line starting with '>'

                genome += line.upper().rstrip()
                        

    return genome

seq = fastaReader('inutil aligned.fas') #bulk read together then split later

seq_split = re.findall('P.*?LNF', seq) #find all sequences #no mutation in the last 3 characters, checked

x = [] #split each sequence into characters

for i in seq_split:
    
    z = [y for y in i]
    
    x.append(z)

seq_dframe = pd.DataFrame (x)

a = list()

for i in range(0,33,2):
    
     a.append(seq_dframe.iloc[i] == seq_dframe.iloc[i+1])

seq_compared = pd.DataFrame(a).astype(int).sum()
seq_compared[seq_compared == seq_compared.min()]