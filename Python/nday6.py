# 2025 - 02 - 03
# Python
import pandas as pd

## User-defined functions
""" 
Arbitrary arguments(*args)
when you do not know the number of arguments that will be used in a function
"""
def echo_list(*args):
    print(args)
    print([x for x in args])

def lang_ver(lang, *args):
    ver_str = ', '.join([str(ver) for ver in args])
    res_str = '%s versions: %s' %(lang, ver_str)
    return res_str


# Quiz
def reverse_complement_list(*args):
    nt_pairH = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    rev_seq_list = []
    for t in [x[::-1] for x in args]:
        rev_seq_list.append(''.join([nt_pairH.get(nt, 'X') for nt in t]))
    return rev_seq_list


# Exception handling - Try ... Except
""" 
if you expect that an error may occur, you can handle the error and proceed the code execution using try-except blokcks.
"""
def add2num(x,y):
    if isinstance(x,(int,float)) and  isinstance(y, (int, float)):
        z = x + y   
        return z
    else:
        print('pleas insert numeric data')
'''
isinstance(object, classinfo)
특정 객체가 특정 데이타 타입(클래스)에 속하는지 확인할 때 사용
object : 객체
classinfo : 검사할 데이터 타입 또는 클래스
반환값 : TRUE, FALSE
'''

def add2num2(x,y):
    try:
        z = float(x) + float(y)   
        return z
    except:
        print('only int/float are allowed')

def add2num_rev(x,y):
    try:
        z = float(x) + float(y)   
        return z
    except:
        print('only int/float are allowed')
    finally:
        print('this function is working')


# Raise an exception
def oddeven(x) :
    if not isinstance(x, (int)) :
        raise Exception(f'Integers are only accepted. your input is {type(x)}')
    elif x % 2 == 1:
        print('x is odd')
    else:
        print('x is even')
'''
Exception 은 모든 예외(에러)의 기본 클래스이다. 사용자 정의 예외를 만들거나 예외를 처리할 때 활용한다.
'''


# Class 
"""Python: an object-oriented programming(OOP) language"""
# class myClass:
#     '''this is a docstring of myClass'''
#     att = 'hello, my world'
#     def helloworld(self):
#         print('hello, world')

a = myClass()
b = myClass()

a.att
a.helloworld()

class myClass:
    def union_set(self, set1, set2):
        result = set1 | set2
        return result
    def inter_set(self, set1, set2):
        result = set1 & set2
        return result

a = myClass()
a.union_set({1,2,3}, {3,4,5})
a.inter_set({1,2,3}, {3,4,5})


class myClass2:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2
    def union_set(self):
        result = self.set1 | self.set2
        return result
    def inter_set(self):
        result = self.set1 & self.set2
        return result

a = myClass2()
a = myClass2({1,2,3}, {3,4,5})
a.union_set()
a.inter_set()


class MySeq:
    '''this is from the textbook'''
    def __init__(self, seq, seq_type = "DNA"):
        self.seq = seq
        self.seq_type = seq_type
    def print_sequence(self):
        print('Sequence: ' + self.seq)
    def get_seq_biotype(self):
        return self.seq_type
    def show_info_seq(self) :
        print('Sequnece: ' + self.seq + " biotype: " + self.seq_type)
    def count_occurrences(self, seq_search):
        return self.seq.count(seq_search)

a = MySeq('AGTCAAAT')
a.print_sequence()
a.get_seq_biotype()
a.show_info_seq()
a.count_occurrences('A')

# class rcClass:
#     nt_pairH = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
#     def __init__(self, orig_seq):
#         self.orig_seq = orig_seq
#         self.temp_seq = self.orig_seq[::-1]
#         self.rev_seq = ''.join([rcClass.nt_pairH.get(nt, 'X') for nt in self.temp_seq])
#     def reverse_complement(self):
#         return self.rev_seq
#     def nt_count(self, count_nt):
#         return self.orig_seq.count(count_nt)
#     def rc_nt_count(self, count_nt):
#         return self.rev_seq.count(count_nt)

a = rcClass('AAAT')
b = rcClass('CCCC')
a.nt_pairH
b.nt_pairH
a.reverse_complement()
b.reverse_complement()
a.nt_pairH['N'] = 'N'
a.nt_pairH
b.nt_pairH

class rcClass:
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

seq1 = rcClass('ATAACCCCGCG')
seq1.reverse_complement()
seq1.nt_count('T')
seq1.rc_nt_count('G')
