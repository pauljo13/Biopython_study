# Python
## Change working directory in python
"""
1. Set working directory in python IDE
2. Change thr current directory
3. Use os.chdir()
"""

import os
print(os.getcwd())
os.chdir('/Users/knu_cgl1/Desktop/Study/')
print(os.getcwd())

## Read and write files
"""
file = open(filename, mode)
- 'r' : open for reading(default)
- 'w' : open for writing(overwrite of the file exists)
- 'a' : open for writing(append)
- 't' : open in text mode(default)
"""
os.chdir('/Users/knu_cgl1/Desktop/Study/Obsidian/Biopython_study')
new_file = open('mytile1.txt', 'w')
new_file.close()

new_file = open('myfile2.txt', 'w')
new_file.write('line number 1\n')
new_file.write('line number 2\n')
new_file.close()

new_file = open('myfile2.txt', 'a')
for i in range(3, 7):
    new_file.write('line number %s\n' % i)

new_file.close()

mylist = ['line number %s' % i for i in range(1,7)]
new_file = open('myfile2.txt', 'w')
new_file.write('\n'.join(mylist))
new_file.write('\n')
new_file.close()


mylist.append('line end.')
with open('myfile2.txt', 'w') as new_file:
    new_file.write('\n'.join(mylist))
    new_file.write('\n')
    

# Quiz
seq = "AATCTCGGCAAA"
cop = {"A":"T","T":"A","C":"G","G":"C"}
# req = []
# for i in range(len(seq)):
#     req.append(cop[seq[i]])
# req = "".join(req)
temp_seq = seq[::-1]
rew_seq = ''.join([cop.get(nt, 'X') for nt in temp_seq])

new_file = open('myseq.txt', 'w')
new_file.write(seq + '\n')
new_file.write(rew_seq + '\n')
new_file.close()


# Read a text file
""" 
1. read(n) - read a string corresponding to the next block of n characters
2. readline(n) - returns the next n characters from the next line
3. readlines() - returns a list of strings with all the lines in the file
"""
print(os.getcwd())
myfile = open('myfile2.txt')
myfile.read()
myfile.close()

myfile = open('myfile2.txt')
myfile.read(3)
myfile.close()

with open('myfile2.txt') as myfile:
    myfile.read()
    
myfile = open('myfile2.txt')
myfile.readlines()
myfile.close()

myfile = open('myfile2.txt')
myfile.readline()
myfile.readline(3)
myfile.close()


myfile = open('myfile2.txt')
while True:
    line = myfile.readline()
    if not line:
        break
    print(line)
myfile.close()

myfile = open('myfile2.txt')
for line in myfile:
    print(line)
myfile.close()

myfile = open('myfile2.txt')
for line in myfile:
    print(line[:-1])
myfile.close()

# Quiz
cop = {"A":"T","T":"A","C":"G","G":"C"}
myseq = open('myseq.txt')
seq = myseq.readlines()
orig_seq = seq[0][:-1]
temp_seq = orig_seq[::-1]
rev_seq = "".join([cop.get(nt,'X') for nt in temp_seq])
if seq[1][:-1] == rev_seq:
    print('they are reverse complement')
else:
    print('they are not reverse complement')
    
    
import pandas as pd
# dt = pd.read_csv('pd_test.txt', sep='\t')
# dt.to_csv('pd_test.csv', seq=",", index=False)

# User-defined dunctions
def myfunc1():
    '''thus us a docstring'''
    #this is a comment

myfunc1.__doc__

def add2num(x, y):
    if isinstance(x, (int,float)) and isinstance(y, (int,float)):
        z = x + y
        return z
    else:
        print('please insert numeric data')

add2num(1.2, 'abc')
add2num(1,2)

def helloworld():
    print('hello, world')
    
    
def echo(whatever):
    print(whatever)

def addsub(x, y):
    a = x + y
    b = x - y
    print(f'{x} + {y} = {a}')
    print(f'{x} - {y} = {b}')
    return (a, b)

helloworld()
echo('hello world')
addsub(7,3)

def welcome(x, y = 'hello'):
    print(f'{x}, {y}')
    
welcome('hj')
welcome('hj', 'hi')
welcome(x = 'hj')
welcome(y= 'bye', x = 'hj')

def welcome_hj(x ='hj', y = 'hello'):
    print(f'{x}, {y}')

welcome_hj()

# def welcome_hj2(x = 'hj', y):
#     print(f'{y}, {x}')

# welcome_hj2('bye')

#Quiz
nt_pairH = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
orig_seq = input('enter your seq: ')
temp_seq = orig_seq[::-1]
rev_seq = ''.join(nt_pairH.get(nt, 'X') for nt in temp_seq)
print(rev_seq)

def reverse_complement():
    orig = input('enter your seq: ')
    rev = "".join(nt_pairH.get(nt, 'X') for nt in orig[::-1])
    print(rev)
    return rev

reverse_complement()