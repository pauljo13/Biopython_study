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
        raise Exception(f'Integers are only accepted. your')