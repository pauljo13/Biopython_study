a = True
if a:
    print('a is true')
b = False
if b:
    print("b is true")

a = 5
if a > 3:
    print('a is greater than 5')

b = [3,5,7]
if a in [3, 5, 7]:
    print('a is one of 3, 5, and 7')

c = 1 
if a == 5 and c == 1:
    print('both statements are true')

if a != 5 or c == 1:
    print('at least one of the statements is true')

a = 5
b = [3, 5, 7]
c = 1
if a == 5 and c == 1:
    print('both statements are true')
else:
    print("at least one of the statements are false")

if a == 5 and c < 1:
    print('both statements are true')
else:
    print('at least one of the statements are false')
    

# Quiz
a = 5
if a % 2 == 0:
    print("b is an even number")
else:
    print("a is an odd number")
    

# Conditional expression
print('a is greater tha c') if a > c else print('a is less than or equals to c')

print('a is less than or equals to c') if not a > c else print('a is greater than c')

# Quiz
x = 28
y = 45

a = x if x > y else y

print(a)

# if elif else
a = 5
b = [3, 5, 7]
if a == 7:
    print('a is 7')
elif a == 3:
    print('a is 3')
elif a in b:
    print('a is 5')
else:
    print('a is not in [3, 5, 7]')
    

# Quiz
book = 10000
coffee = 3000
candy = 500

cash = 4500
basket = []

if cash >= book:
    cash -= book
    basket.append('book')
elif cash >= coffee:
    cash -= coffee
    basket.append('coffee')
elif cash >= candy:
    cash -= candy
    basket.append('candy')
else:
    "there is nothing I can afford."
print(basket)

# while 
n = 10
i = 0
while i < n :
    i += 2
    print(i)

# while ... else
i = 0
n = 10

while i < n:
    i += 1
    print(f'{i}  is M= {n}')
else:
    print('now i is greater than n')

# Infinite loops
# a = True
# while a:
#     print('if you want to escape the loop, press "ctrl+c"')

# Nested while loops
n = 5
i = 0
while i < n:
    i += 1
    j = 0
    while j < i :
        j+= 1
        print('i = %s, j = %s' %(i,j))

# while + if
n = 10
i = 0
oddList = []
evenList = []

while i < n :
    i += 1
    if i % 2 == 1:
        oddList.append(i)
    else:
        evenList.append(i)
print(oddList)
print(evenList)

# Quiz
n = 100
i = 0
ans = 0

while i < n:
    i += 1
    if i % 7 == 0:
        ans += i
    else:
        continue
print(ans)

# break
"""Break statement terminates the loop"""
a = 'this is a string'
idx = 0

while idx < len(a):
    if a[idx] == ' ':
        print('spaces are not allowed')
        break
    else:
        print(a[idx])
    idx += 1

# Quiz
mylist = ['watermelon', 'banana', 'apple', 'tomato', 'peach']
vege_list = ['tomato', 'carrot', 'radish']

i = 0
while mylist:
    x = mylist.pop()
    if x in vege_list:
        print(x,"is in vege_list")
        break
    else:
        print(x)

# continue
"""Continue statement skip the code inside the loop"""
a = "this is a string"
idx = 0

while idx < len(a):
    if a[idx] == ' ':
        print('spaces are not printed')
        idx += 1
        continue
    else:
        print(a[idx])
    idx += 1

mylist = ['watermelon', 'banana', 'apple', 'tomato', 'peach']
vege_list = ['tomato', 'carrot', 'radish']

i = 0
while mylist:
    x = mylist.pop()
    if x in vege_list:
        continue
    else:
        print(x)


# while
n = 10
i = 0

while i < n :
    i += 2
    print(i)

l = [i for i in range(2,11,2)]
for i in l:
    print(i)

# range
## Range - range(start, end, step)
print(range(5))
print(type(range(5)))
print(range(1,5))
print(range(1,5,2))

# for
for i in range(2, 11, 2):
    print(i)

# for + if
n = 10
i = 0
oddList = []
evenList = []

while i < n:
    i += 1
    if i % 2 == 1:
        oddList.append(i)
    else:
        evenList.append(i)
print(oddList)
print(evenList)

oddList = []
evenList = []
for i in range(1,11):
    if i % 2 == 1:
        oddList.append(i)
    else:
        evenList.append(i)

print(oddList)
print(evenList)

# Quiz
s = 0
for i in range(1,101):
    if i % 7 == 0 and i % 2 == 0:
        s += i
    else:
        pass
print(s)

a = "this is a string"
for i in a:
    if i == ' ':
        print('spaces are not allowed')
        break
    else:
        print(i)

a = "this is a string"
for i in a:
    if i == ' ':
        print('spaces are not allowed')
        continue
    else:
        print(i)

# Quiz
mylist = ['watermelon','banana','apple','tomato','peach']
o_list = []

for i in mylist:
    if 'o' in i:
        o_list.append(i)
    else:
        pass
print(o_list)

# for - range
a = "this is a string"
idx_space = []
for i in range(len(a)):
    if a[i] == ' ':
        idx_space.append(i)
print(idx_space)    

# Quiz
mylist = ['watermelon','banana','apple','tomato','peach']
