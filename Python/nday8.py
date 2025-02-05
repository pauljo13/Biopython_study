#2025-02-05
import sys
sys.path.append('C:/Users/user/Desktop/Python/Python')

import mod1
mod1.helloworld()

import os
os.getcwd()

sys.path.append('/Users/knu_cgl1/Desktop/Study/Obsidian/Biopython_study/Python')  
sys.path

import mod1
seq1 = mod1.rcClass('ATAACCCGCG')
print(seq1.reverse_complement())


# Quiz
import mod1
class rcClassChild3(mod1.rcClassChild):
    def tatio_T(self, count_nt = 'T'):
        return abs(super().nt_ratio(count_nt) - super().rc_nt_ratio(count_nt))

seq1 = rcClassChild3('ATAACCCCGCG')
print(seq1.tatio_T())


# Running the python script
# Practice
myDir = '/Users/knu_cgl1/Desktop/Study/Obsidian/Biopython_study/Python'
import os, sys
import random
import math
print(os.getcwd())
sys.path.append(myDir)
import myfuncs as mf

for i in range(10):
    print(random.choice(range(1, 20)))

random.choices(range(1, 20), k = 5)
random.choices(range(1, 5), k = 10)

# 1. Generate 1000 x 20nt-sequences and write them in a new text file.
outfile = open('%s/BIC0711_practice1/random_20nt_seq_1000.txt' % myDir, 'w')

for i in range(1000):
    seq = ''.join([random.choice('ATGC') for j in range(20)])
    outfile.write(seq + '\n')

outfile.close()

# 2. get reverse complement sequences of the generated random sequences and binds them as a new column.
infile = open('%s/BIC0711_practice1/random_20nt_seq_1000.txt' % myDir, 'r')
outfile = open('%s/BIC0711_practice1/random_20nt_seq_1000_rc.txt' % myDir, 'w')

# 1)
for line in infile:
    orig_seq = line[:-1]
    rec_seq = mf.rcClass.reverse_complement(orig_seq)
    outfile.write(orig_seq + '\t' + rec_seq + '\n')

# 2)
orig_seq_list = infile.readlines()
rec_seq_list = [mf.rcClass.reverse_complement(seq[:-1]) for seq in orig_seq_list]
result_list =  ['%s\t%s\n' % (x[:-1], y) for x, y in zip(orig_seq_list, rec_seq_list)]
outfile.writelines('\n'.join(result_list) + '\n')

infile.close()
outfile.close()


# Zip : aggregate iterables in a tuple
a = [1, 2, 3]
b = ['one', 'two', 'three']
zip(a, b)
print(list(zip(a, b)))
[str(x) + y for (x, y) in zip(a,b)]
c = ('i', 'ii', 'iii')
print(list(zip(a, b, c)))

a = [1,2]
b = range(1, 11)
print(list(zip(a, b)))