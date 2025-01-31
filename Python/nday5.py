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

