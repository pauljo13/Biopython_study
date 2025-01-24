a = "Python"
print(f"Hi, {a}")

a = 'I need to study Python'
lang = "Python"
ver = 2.7

print(f"I need to study {lang}{ver}")
print(f"I need to study {lang}{ver:.2f}")
print(f"I need to study {lang}{ver+1}")
print(f"I need to study {a[16:]}{ver+1}")

# Quiz
import math
p = "pi"
pi = math.pi
print(f"The ratio of a circle's circumference to its diameter is called {p}, and the value of {p} is {pi:.2f}")

a = "How many white-spaces in this sentence?"
print(a)
print(a.count(' '))
print(a.count('h'))

# (r)find & (r)index - stringname.find(substring, start, end)
seq = "ATCGATCGAAAA"
print(seq)
print(seq.count('T'))
print(seq.find('T'))
print(seq.find('AAA'))
print(seq.find('N'))
print(seq.index('T'))
print(seq.index('N'))

# Quiz
a = "AATCAAAACCGAATTTTT"
for i in ["A", "T", "C", "G"]:
    print(f"{i} : {a.count(i)} / {len(a)}")
    print(f"== {a.count(i)/len(a):.2f}")

# Useful functions for string
## join - "character to be joined".join(stringname)

print(seq)
print('\t'.join(seq)) #\t : 탭
print(' '.join(seq))
print('\n'.join(seq)) #\ㅜ : 줄바꿈

## strip = stringname.(lr)strip('character be stripped')
a = f'{"ATCG":^10}'
print(a)
print(a.strip())
print(a.lstrip())
print(a.rstrip())
a = f'{"ATCG":!^10}'
print(a)
print(a.strip("!"))

## replace = stringname.replace(old text, new text, count)
print(a)
print(a.replace('!', '?'))
print(a)
a2 = a.replace('!', '?')

# Quiz
seq = "ATCGATCG\n"
seq = seq.strip("\n")
print(seq)
seq2 = seq.replace("C", "c")
print(seq2)

# Useful functions for string
## split : stringname.split(separator, max)
a = 'A\tT\tC\tG\tA\tT\tC\tG\tA\tA\tA\tA'
print(a)
print(a.split('\t'))

# Quiz
a = ",".join('ATCG')
print(a)
print(a.split(','))

print([])
print(type([]))
print([1,2,3])
print(["a", "b", "c"])
print(["a", "b",1, 2])
print(["a", "b",[1, 2]])
print([1, 2] + ["a", "b"])
print([1, 2] + ["a", "b"] + [["a"]])
print([1, 2] + ["a", "b"] + [["a"]]*2)

print(len([1,2]))
print(len([1, 2] + ["a", "b"]))
print(len([1, 2] + ["a", "b"] + [["a"]]))
print(len([1, 2] + ["a", "b"] + [["a"]]*2))

# Indexing & splicing in list
a = "I need to study Python".split()
print(a)
print(a[0])
print(a[4])
print(a[0] + a[4])
print(a[4][:4])
print(a[0, 4])

print(a[:])
print(a[3:5])
print(a[:3])
print(a[4:])
print(a[::-1])

print(a)
print(a[4])
a[4] = "Java"
print(a[4])
print(a)

del a[4]
print(a)

a += ['Python', [2.7, 3.7]]
print(a)

print(a[5])
print(a[5][0])
print(a[5][:1])
print(type(a[5][0]))
print(str(a[5][0]))
print(str(a[5][0])[2])

# Quiz
a = [1, 2, [3, 4, 5], 6, ['7', '8']]
print(a[3])
print(a[2][2])
print(a[4][0])
print(a[2][1:])

# Useful functions in list
## Join - "character to be joined".join(list)
a = ['A', 'T', 'C', 'G']
print(a)
print(":".join(a))
print("\n".join(a))

## Count - list.count(element)
a = []
for i in range(1, 5):
    for j in range(i):
        a.append(i)
print(a)
print(a.count(1))
print(a.count(4))

## Append - list.append(item
a = "A T C G".split(" ")
print(a)
a.append("N")
print(a)
a.append("A T C G".split(" "))
print(a)
a.append("A", "T")
print(a)

## Extend - list.extend(iterable)
a = "A T C G".split(" ")
print(a)
a.append(["N"])
print(a)
a.extend(["N"])
print(a)

