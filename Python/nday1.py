# Types of operators
# sum
print(1 + 2)

# difference
print(2 - 4)

# multiplication
print(3 * 4)

# division
print(4 / 3)

# exponentiation
print(2 ** 4)

# integer division
print(4 // 3)

# remainder of the integer division
print(5 % 3)

# Mathematical functions

print("abs(-3) :", abs(-3))
print("round(3.4) :", round(3.4))
print("round(3.6) :", round(3.6))
print("pow(2, 4) :", pow(2, 4))
print("int(3.4) :", int(3.4))
print("float(3) :", float(3))

# Module math
import math

math.sqrt(16)

math.log(10)

math.log10(10)

math.log2(10)

# Quiz
print(math.log2(128) // 3,"\n",math.log2(128) % 3)

a = 1
b = 2
print(a + b)

a = math.log2(16)
b = round(3.6)
print(a / b)

a = 3
b = float(a)
print("a : ", type(a))
print("b : ", type(b))

a = 2
b = 2
c = 2
li = [a, b, c]
for i in li:
    print(i)

a = b = c = 3
li = [a, b, c]
for i in li:
    print(i)
    
a, b, c = 1, 2, 3
li = [a, b, c]
for i in li:
    print(i)

# Quiz
a, b = math.log2(128), math.log2(256)
print("a :", a, "/ b :", b)
c = a * b
print("c :", c)

a = 1
a == 1

a = b = 2
a == b

c = 3
a == b

a == b == c

b == c

a == b != c

# Quiz
print(2**3 == 8)
print(pow(2,3) == 8)
print(math.pow(2,3) == 8)


# Other operators
"+= equals to x = x + y"
a = 1
a = a + 2
a

a = 1
a += 2
a

a = 2 
a = a - 1
a 

a = 2
a -= 1
a

a *= 3
a

a /= 3
a

'''This 
is
a
string'''

"""This 
is
a
string"""

print('I love "python"')

print("I love 'python'")

print("I love \"python\" ")

a = "python"
a

a = '1'
b = '2'
a + b

print("python" * 3)

'pythonpythonpython'

print(len("pythonpythonpython"))

a = "I need to study Python"
len(a)

# Quiz
q = "Hello, world!"
print(len(q))
if len(q) % 2 == 0:
    print("짝수")
else:
    print("홀수")

# Indexing & splicing
a = "I need to study Python"
print(a[0])
print(a[16])
print(a[-1])
print(a[-22])

print(a[16:21])
print(a[16:22])
print(a[16:22:2])
print(a[::-1])
print(a[16:len(a)])
print(a[16:])
print(a[16:-1])
print(a[0:9])
print(a[:9])
print(a[:-13])

prefix = a[:9]
verb = a[10:15]
obj = a[16:]

print(prefix + " " + verb + " " + obj)

# Quiz
q = 'DNA nucleotides consist of "ATCG" '
print(len(q))
print(q[27::])
print(q[28:-1])
print(q[::-1][2:6])
print(q[28:-2][::-1])

a[16:] = "Java"

obj = "Java"
a = prefix + " " + verb + " " + obj
print(a)
print(len(a))

for i in ['Python', 'Java']:
    print('I need to study %s' %i)

print('I need to study Python%d' %3)
print('I need to study Python%d' %2)
print('I need to study Python%f' %2.7)
print('I need to study Python%s' %2.7)
print('I need to study Python%.1f' %2.7)

print("humans share about %s% of DNA with chimpanzees" %99)

print("humans share about %s%% of DNA with chimpanzees" %99)

print('I need to study Python%.1f' %2.7)
print('I need to study Python%5.1f' %2.7)
print('I need to study Python%2.1f' %2.7)

lang = "Python"
ver="2.7"
print("I need to study " + lang + ver)
print("I need to study %s%s"  %(lang , ver))

# Quiz
""" 
%s, %f, math.pi를 이용하여 아래와 같은 문구가 나오도록 명렬어를 작성해보시오.
"""

print("The ratio of a circle’s circumference to its diameter is called %s, and the value of %s is %.2f" % ('pi', 'pi', math.pi))


