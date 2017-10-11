# handle_fasta_file.py
# Created by kxyu on 17-10-9

''' Question
1) Read sample_seq.txt using Perl or Python, filter non-ATGC bases;
 
2) Translate DNA sequences to Proteins;
 
3) Count the unique proteins and compute the frequency of occurrency;
 
4) Find the proteins with the keywords IGHV4-4 and IGHJ4.
 
the final output file format(fasta):  >Id|frequency|length of protein|keywords  prtein sequence
'''

import sys

Termination_codon=["TGA","TAG","TAA"]

AA_codon = {'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_',
            'TAG':'_', 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P',
            'CCG':'P', 'CCT':'P', 'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'ATA':'I',
            'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
            'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A',
            'GCT':'A', 'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G'}
seq ={}

file_write = open(r'C:\Users\ykx\PycharmProjects\test\Output.fasta', 'w')
#file_write = open(sys.argv[2], 'w')

with open(r'C:\Users\ykx\PycharmProjects\test\sample_seq.fasta', 'r') as file_read:
#with open(sys.argv[1], 'r') as file_read:
    for line in file_read.readlines():
        if line.__eq__('\n'):
            break
        if line.startswith('>'):
            name = line.replace('>', '').split()[0]
            seq[name]= '1'
        else:

            isFilter = False

            for i in line.replace('\n', ''):
                if not 'ATGC'.__contains__(i):

                   isFilter = True
                   seq.pop(name)

            if isFilter is True:
                continue

            seq[name] = line.replace('\n', '')

for key in seq.keys():

    mAA_seq = ''

    if str(key).__contains__('IGHV4-4') and str(key).__contains__('IGHJ4'):

     mNC_len = len(seq[key])

     for i in range(0, mNC_len, 3):

        if seq[key][i:i + 3] in Termination_codon:
            break

        if seq[key][i:i + 3] in AA_codon:
            mAA_seq += AA_codon[seq[key][i:i + 3]]

     mAA_seq_len = len(mAA_seq)
     mFrequency = round(mAA_seq_len / mNC_len, 2)

     txt = '>'+key+'|'+str(mFrequency)+'|'+str(mAA_seq_len)+'|'+mAA_seq+'\n'+seq[key]+'\n'
     file_write.write(txt)


file_write.close()