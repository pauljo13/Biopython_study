a = "A T C G".split(" ")
a.sort()
print(a)

a.sort(reverse=True)
print(a)

a = ['9', '87', '654', '3210']
print(a)
print(sorted(a))
print(sorted(a, reverse=True))
print(sorted(a, key=len))
print(a)

# Reverse - list.reverse()
a = "A,T,C,G".split(',')
a.reverse()
print(a)
a = "A,T,C,G".split(',')
print(a[::-1])
print(a)

# index - list.index(element, start, end)
print(a)
print(a.index('A'))
a.append('A')
print(a.index('A'))
a.append(['N'])
print(a)
print(a.index('N'))
print(a.index(['N']))

# insert - list.insert(index, item)
a = [i for i in range(0,4)]
print(a)
a.append(-1)
print(a)
a.insert(0, -1)
print(a)
a.insert(2,.5)
print(a)

# Insert - list.remove(element)
print(a)
del a[0]
print(a)
a.insert(0,-1)
print(a)
a.remove(-1)
print(a)
a.remove(-1)
print(a)
a.remove(4)


# Quiz
a = "I do not need to study programming".split(" ")
not_index = a.index("not")
print(a)
del a[not_index]
print(a)
a = "I do not need to study programming".split(" ")
a.remove("not")
print(a)

# pop - list.pop(index)
a = [i for i in range(5)]
print(a.pop())
print(a)
print(a.pop(2))
print(a)
a_idx1 = a.pop(1)
print(a)
print(a_idx1)

# Copy - list.copy()
a = [i for i in range(4)]
b = a
print(b)
a.pop(0)
print(a)
print(b)


a = [i for i in range(4)]
b = a.copy()
print(b)
a.pop(0)
print(a)
print(b)

print(())
print(type(()))
a = (1, 2, 3)
b = ('a', 'b', 'c')
print(a)
print(b)
print(('a', 'b', 1, 2))
print(('a', 'b',[1,2]))
print(('a', 'b',[1,2],(3,4)))

a = "this is a tuple not list".split(" ")
a = tuple(a)
print(a)
print(a[0])
print(a[2:])
print(a[-1])
a[-1] = "string"

a.append("string")

a = [i for i in range(1,9)]
print(a)
print(set(a))
print(list(set(a)))

a = (1, 2, 2, 3)
print(set(a))

# To obtain intersect of union of two sets
a = set([i for i in range(1,4)])
b = set([i for i in range(3,6)])
print(a & b)
print(a | b)
print(a - b)
print(a ^ b)

# Quiz 
a = [i for i in range(2, 13, 2)]
b = tuple([i for i in range(3, 16, 3)])
c = list(set(a) & set(b))
c.sort()
print(a)
print(b)
print(c)


dict_a = {'a': 1, 'b': 2, 'c': 3, "z": 26}
print(len(dict_a))
dict_a['y'] = 25
print(dict_a)
dict_a['ab'] = (1,2)
print(dict_a)
dict_a[['a', 'b']] = [1,2]

dict_a[('a', 'b')] = [1, 2]
print(dict_a)
del dict_a['a']
print(dict_a)

# Get value using key in dictionary
a = {1: 'one', 2: 'two', 3: 'three'}
print(a[1])
print(a['1'])

# dict.get(key, value)
print(a.get(1))
print(a.get('1', 'no such key in this dictionary'))

# dict.keys()
a = {1: 'one', 2: 'two', 3: 'three'}
print(a.keys())
a_key_list = list(a.keys())
print(a_key_list)

# dict.values()
print(a)
print(a.values())
a_value_list = list(a.values())
print(a_value_list)

# dict.items()
print(a)
print(a.items())
a_item_list = list(a.items())
print(a_item_list)
print(a_item_list[0])
print(a_item_list[0][0])
print(a_item_list[0][1])

# dict.updatae(new)
print(a)
a.update({4: 'four'})
print(a)
a2 = {2: 'two', 5: 'five'}
print(a + a2)

a.update(a2)
print(a)

# Quiz
gene_func_dict = {'EGFR': 'oncogene', 'KRAS': 'oncogene', 'PTEN': 'TSG', 'GAPDH': 'house', 'ACTB': 'house'}
print(len(gene_func_dict.keys()))
print(sorted(list(gene_func_dict.keys())))
print(len(set(gene_func_dict.values())))

# in / not in
print('a' in 'abcdeg')
print('a' in ['abc'])
print('a' not in ('abc', 'def'))
print('abc' in ('abc', 'def'))
print("GAPDH" in gene_func_dict.keys())

# Quiz 
gene_func_dict = {'EGFR': 'oncogene', 'KRAS': 'oncogene', 'PTEN': 'TSG', 'GAPDH': 'house', 'ACTB': 'house'}
def gene_is_in(gene, value=None):
    if gene in gene_func_dict.keys():
        print(gene_func_dict[gene])
    else:
        gene_func_dict[gene] = value
        print(gene_func_dict)


print(gene_func_dict)
gene_is_in('EGFR')
print('='*10)
gene_is_in('ERBB2','oncogene')