# 2025-02-06
# Practice
myDir = '/Users/knu_cgl1/Desktop/Study/Obsidian/Biopython_study/Python'
import os, sys
import random
import math
print(os.getcwd())
sys.path.append(myDir)
import myfuncs

outfile = open('%s/BIC0711_practice1/random_20nt_seq_1000.txt' % myDir, 'w')

for i in range(1000):
    seq = ''.join([random.choice('ATGC') for j in range(20)])
    outfile.write(seq + '\n')

outfile.close()

# 2. get reverse complement sequences of the generated random sequences and binds them as a new column.
infile = open('%s/BIC0711_practice1/random_20nt_seq_1000.txt' % myDir, 'r')
outfile = open('%s/BIC0711_practice1/random_20nt_seq_1000_rc.txt' % myDir, 'w')

orig_seq_list = infile.readlines()
rec_seq_list = [myfuncs.rcClass(seq[:-1]).reverse_complement() for seq in orig_seq_list]
result_list =  ['%s\t%s' % (x[:-1], y) for x, y in zip(orig_seq_list, rec_seq_list)]
outfile.writelines('\n'.join(result_list) + '\n')

infile.close()
outfile.close()

sys.path.append('/Users/knu_cgl1/Desktop/Study/Obsidian/Biopython_study/Python')
import myfuncs
class newClass(myfuncs.rcClassChild2):
    def nt_ratio_all(self, type = 'orig'):
        res = {}
        for nt in ['A', 'T', 'G', 'C']:
            if type == 'orig':
                res[nt] = self.nt_ratio(nt)
            elif type == 'rev':
                res[nt] = self.rc_nt_ratio(nt)
            else:
                raise Exception(f'type should be "orig" or "rev", your input {type}')
        return res

infile = open('%s/BIC0711_practice1/random_20nt_seq_1000.txt' % myDir, 'r')
outfile = open('%s/BIC0711_practice1/random_20nt_seq_1000_rc2.txt' % myDir, 'w')

outfile.write('Oringinal\tRevere complement\torig_A\torig_T\torig_C\torig_G\trev_A\trev_T\trev_C\trev_G\n')

for line in infile:
    orig_seq = line[:-1]
    seq_cls = newClass(orig_seq)
    rec_seq = seq_cls.reverse_complement()
    oring_seq_ratio = seq_cls.nt_ratio_all('orig')
    rev_seq_ratio = seq_cls.nt_ratio_all('rev')
    outfile.write(orig_seq + '\t' + rec_seq + '\t')
    outfile.write('\t'.join(['%s' % oring_seq_ratio[nt] for nt in ['A', 'T', 'C', 'G']]) + '\t' + '\t'.join(['%s' % rev_seq_ratio[nt] for nt in ['A', 'T', 'C', 'G']]) + '\t' )
    outfile.write('\t'.join(['%s' % rev_seq_ratio[nt] for nt in ['A', 'T', 'C', 'G']]) + '\t' + '\t'.join(['%s' % rev_seq_ratio[nt] for nt in ['A', 'T', 'C', 'G']]) + '\n' )

infile.close()
outfile.close() 

# Practice 4.
# 4-1. Determine if there are any duplicated sequences
infile = open('%s/BIC0711_practice1/random_20nt_seq_1000_rc2.txt' % myDir, 'r')
seq_list = infile.readlines()

print(any(seq_list.count(seq) > 1 for seq in seq_list))

print(len(set(seq_list)) != len(seq_list))

infile.close()


# Practice 5.
#5. Generate 10000 X 30-35nt of random sequences. Write them in a new text file.

outfile = open('%s/BIC0711_practice1/random_randnt_seq_10000.txt' % myDir, 'w')

for i in range(10000):
    num_k = random.choice(range(30, 36))
    rdm_seq = ''.join(random.choices('ATCG', k = num_k))
    outfile.write(rdm_seq + '\n')

outfile.close()

# Practice 6. log2-transformation
## 데이터 입력과 출력 파일 설정
inExprFile = open(f'{myDir}/BIC0711_practice1/GSE16659_series_matrix.txt', 'r')
outExprFile = open(f'{myDir}/BIC0711_practice1/GSE16659_series_matrix_log2.txt', 'w')

## 메타데이터 부분을 읽기
while True:
    line = inExprFile.readline()
    dataL = line.rstrip('\n').split('\t') # 탭으로 분리
    if dataL[0] == '!Sample_title': # 샘플 제목 저장
        headerL = dataL.copy()
    elif dataL[0] == '"ID_REF"': #유전자 타침 ID을 만나면 종료
        break

outExprFile.write('\t'.join(headerL) + '\n') # 샘플 제목을 기록

# 유전자 발현값을 log2로 변환하여 기록
for line in inExprFile:
    if line[0] == '!': # !: 메타데이터 부분으로 해당 행들을 무시
        continue
    dataL = line.rstrip('\n').split('\t') # 탭으로 분리
    lg2_valueL = ['%.2f' % math.log2(float(value) + 1) for value in dataL[1:]] # log2 변환
    outExprFile.write('%s\t%s\n' % ( dataL[0], '\t'.join(lg2_valueL))) # 유전자 ID와 log2 변환값을 기록

outExprFile.close()
inExprFile.close()
    
# Practice 7. plot histogram
with open(f'{myDir}/BIC0711_practice1/GSE16659_series_matrix.txt', 'r') as inFile_raw:
    val_raw = [line[:-1].split('\t')[1] for line in inFile_raw if line[0] == '"']

def isfloat(x):
    try:
        float(x)
        return True
    except:
        return False

val_raw2 = [float(x) for x in list(filter(isfloat, val_raw))]


with open(f'{myDir}/BIC0711_practice1/GSE16659_series_matrix_log2.txt', 'r') as inFile_new:
    val_new = [float(line[:-1].split('\t')[1]) for line in inFile_new if line[0] == '"']

# Filter(function, iterable) : iterable에서 function이 True인 것만 걸러내어 반환
def isPositive(x):
    return x >= 0

a = filter(isPositive, [-1, 0, 1, 2, 3, -2, -3])
a = list(a)
print(a)

# Matplotlib
from matplotlib import pyplot as plt
plt.hist(val_raw2)
plt.xlabel('Gene expression')
plt.ylabel('Frequency')
plt.title('Raw distribution')
plt.show()