# Introduction to Python 2
## Quiz
mylist = ['watermelon','banana','apple','tomato','peach']
o_idx_list = []
for i in range(len(mylist)):
    if 'o' in mylist[i]:
        o_idx_list.append(i)
print(o_idx_list)


## enumerate
print(mylist)
enumerate(mylist)
for x in enumerate(mylist):
    print(x)
"""(index of  each item, item)"""

print(mylist)
o_idx_list = []
for x in enumerate(mylist):
    (idx, val) = x
    if 'o' in val:
        o_idx_list.append(idx)
    else:
        print(f"'o' is not in {val}")
print(o_idx_list)

## List comprehension
x = 29
y = 45
li = [x if x > y else y]
print(li)

seq = "ATCG"
reslist = []
for i in range(len(seq)):
    val = 'sequen %s: "%s"' % (i+1, seq[i])
    reslist.append(val)
reslist

reslist_2 = ['sequen %s: "%s"' % (i+1, seq[i]) for i in range(len(seq))]
print(reslist_2)
print(reslist == reslist_2)

a = "this is a string"
idx_space = []
for i in range(len(a)):
    if a[i] == " ":
        idx_space.append(i)
print(idx_space)

idx_space2 = [i for i in range(len(a)) if a[i] == " "]
print(idx_space2)
print(idx_space == idx_space2)

## Quiz 
print(mylist)
o_idx_list = []
o_idx_list = [ i for i in range(len(mylist)) if 'o' in mylist[i]]
print(o_idx_list)

# for
for a in [('1', '2'), ('3', '4')]:
    print(a)

for (a, b) in [('1', '2'), ('3', '4')]:
    print(a,b)
    
# Useful functions in dictionary
### dict.items()
a = {1: 'one', 2: 'two', 3: 'three'}
a.items()
a_items_list = list(a.items())
print(a_items_list)
print(a_items_list[0])
print(a_items_list[0][0])
print(a_items_list[0][1])

## for
a = {1: 'one', 2: 'two', 3: 'three'}
a.items()
for (key, value) in a.items():
    print(key, value)

for (key, value) in a.items():
    if value == 'three':
        print(key)

print([key for (key, value) in a.items() if value == 'three'])


# Kwy <-> value in dictionary using "for"
### Dictionary comprehension
a = {1: 'one', 2: 'two', 3: 'three'}
print({value: key for (key, value) in a.items()})

## for
gene_func_dict = {'EGFR': 'oncogene', 'KRAS': 'oncogene', 'PTEN': 'TSG', 'GAPDH': 'house', 'ACTB': 'house'}
for g in ["EGFR", "ERBB2"]:
    if g in gene_func_dict.keys() :
        print(f'{g}: {gene_func_dict[g]}')
    else:
        print(f'{g}: not in gene_func_dict, update "{g}"')
        gene_func_dict[g] = 'oncogene'
print(gene_func_dict)

onco_list =  [i for i in gene_func_dict.keys() if gene_func_dict[i] == 'oncogene']
print(onco_list)

# Kwy <-> value in dictionary using "for/if"
print(gene_func_dict)
print({func: gene for gene, func in gene_func_dict.items()})

new_dict = {}
for gene, func in gene_func_dict.items():
    if new_dict.get(func, -1) == -1:
        new_dict[func] = [gene]
    else:
        new_dict[func].append(gene)
    print(new_dict)
    
    
## Get value using key in dictionary
### dict.get(key, value)
a = {1: 'one', 2: 'two', 3: 'three'}
print(a[1])
print(a['1'])
print(a.get(1))
print(a.get('1'))
print(a.get('1', 'no such key in this dictionary'))


## Example - get reverse complement of DNA strand
nt_pairH = {'A': 'T', 'T': 'A', 'C': 'G', 'G':'C'}

oring_seq = input('enter your seq: ')
temp_seq = oring_seq[::-1]
print(temp_seq)
rev_seq = ''.join([nt_pairH.get(nt,'X') for nt in temp_seq])
print(rev_seq)