# 2025-02-04
# Class
result = 0
def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))
print(add(3))

result2 = 0
def add2(num):
    global result2
    result2 += num
    return result2

print(add2(3))
print(add2(7))

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
print(cal1.add(3))
print(cal1.add(7))
print(cal2.add(4))
print(cal2.add(4))

class FourCal:
    def __init__(self, num1, num2):
        self.first, self.second = num1, num2
    # def setdata(self, num1, num2): # 매서드 호출 보다는 생성자를 구현하는 방법이 안정적
    #     self.first, self.second = num1, num2
    def add(self):
        return self.first + self.second
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return int(self.first / self.second)

a = FourCal(4,2)
# a.setdata(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(a.first)
print(a.second)

id(a.first) # a의 first 주소 값을 확인
id(a.second) 

# Constructor : 객체가 생성될 때 자동으로 호출되는 메서드
# a = FourCal()
# a.add()

a = FourCal(7, 3)
a.add()


# Inheritance
class parentClass1():
    pass

class childClass(parentClass1):
    '''docstring'''
    pass


class rcClass():
    nt_pairH = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    def __init__(self, orig_seq):
        self.orig_seq = orig_seq
        self.temp_seq = self.orig_seq[::-1]
        self.rev_seq = ''.join([rcClass.nt_pairH.get(nt, 'X') for nt in self.temp_seq])
    def reverse_complement(self):
        return self.rev_seq
    def nt_count(self, count_nt):
        return self.orig_seq.count(count_nt)
    def rc_nt_count(self, count_nt):
        return self.rev_seq.count(count_nt)

class rcClassChild(rcClass):
    def nt_ratio(self, nt):
        return self.orig_seq.count(nt) / len(self.orig_seq)
    def nt_count(self, count_nt):
        if self.orig_seq.count(count_nt) == 0:
            print(f'"{count_nt}" is not in "{self.orig_seq}"')
        else:
            return self.orig_seq.count(count_nt)
    def rc_nt_ratio(self, count_nt):
        return super().rc_nt_count(count_nt) / len(self.rev_seq)

seq1 = rcClassChild('ATAACCCCGCG')
seq1.reverse_complement()
seq1.nt_count('N')

class rcClassChild2(rcClassChild):
    def __init__(self, orig_seq):
        self.orig_seq = orig_seq.upper()
        self.temp_seq = self.orig_seq[::-1]
        self.rev_seq = ''.join([rcClass.nt_pairH.get(nt, 'X') for nt in self.temp_seq])

# parent Class의 메서드를 child class가 사용할 수 있다.
# 하지만 parent class는 child class의 메서드를 사용할 수 없다.
a = rcClassChild('aata')
a.reverse_complement()
b = rcClassChild2('aata')
b.reverse_complement()

# class rcClassChildNew(rcClass):
#     def nt_count(self, count_nt):
#         if self.orig_seq.count(count_nt) == 0:
#             print(f'"{count_nt}" is not in "{self.orig_seq}"')
#         else:
#             return self.orig_seq.count(count_nt)
#     def nt_ratio1(self, count_nt):
#         return self.nt_count(count_nt) / len(self.orig_seq)
#     def nt_ratio2(self, count_nt):
#         return super().nt_count(count_nt) / len(self.orig_seq)
#     def nt_nt_ratio3(self, count_nt):
#         return super().rc_nt_count(count_nt) / len(self.rev_seq)


# seq1 = rcClassChildNew('ATAACCCCGCG')
# seq1.nt_ratio1('N')
# seq1.nt_ratio2('N')
# seq1.nt_nt_ratio3('T')

# Quiz
class rcClassChild3(rcClassChild):
    def tatio_T(self, count_nt = 'T'):
        return abs(super().nt_ratio(count_nt) - super().rc_nt_ratio(count_nt))

seq = rcClassChild3('ATAACCCCGCG')
seq.tatio_T()


# Module
""" 
A file containing a set of functions you want to include in your application.
함수나 변수 또는 클래스를 모아 놓은 파일이다.
"""
import os

print(os.getcwd())
new_path = "/Users/knu_cgl1/Desktop/Study/Obsidian/Biopython_study/Python"
os.chdir(new_path)
print(os.getcwd())

import sys
module_path = "/Users/knu_cgl1/Desktop/Study/Obsidian/Biopython_study/Python"
sys.path.append(module_path)    

import mod1
mod1.helloworld()
mod1.echo('Hi~')

from mod1 import helloworld
helloworld()
echo('Hi~')

from mod1 import helloworld, echo
helloworld()
echo('Hi~')

from mod1 import * 
helloworld()
echo('Hi~')
addsub(3, 4)


sys.path.append(module_path)
import mod1
a = mod1.rcClassChild('ATAACCCCGCG')
a.reverse_complement()