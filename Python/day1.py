### 설치 확인
##### 설치 : !pip install biopython
import Bio
print(Bio.__version__)

from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
text = "AGTACACTGGT"
my_seq

text
# 출력함수를 사용하지 않은 경우 문자열과 다르게 출력된다.

# 출력함수를 사용하는 경우 기존의 문자열과 동일하게 출력된다.
print("Seq :", my_seq)
print("Text :", text)

# type으로 데이터의 형태를 출력하면 확실히 다르다는 것을 알 수 있다.
print(type(my_seq))
print(type(text))

for i, l in enumerate(my_seq):
    print("%i %s" % (i, l))

print("="* 7)

for i, l in enumerate(text):
    print(f"{i} {l}")

# 문자열과 동일하게 len()으로 길이를 반환 받을 수 있다.
print(len(my_seq))
print(len(text))

# 인덱스 호출도 시퀀스의 요소에 접근할 수 있다.
print(my_seq[0])
print(my_seq[2])
print(my_seq[-1])

print("AAAA".count("AA")) #Str
print(Seq("AAAA").count("AA")) #Sep

my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print("Len : ", len(my_seq))
print("G : ", my_seq.count("G"))
print("GC% :",100 * (my_seq.count("G") + my_seq.count("C")) / len(my_seq),"%")


# Bio.SeqUtils의 gc_fraction 통해 간단하게 GC 비율을 구할 수 있다.
from Bio.SeqUtils import gc_fraction
print(gc_fraction(my_seq))

my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
my_seq[4:12]

my_seq[0::3]

my_seq[1::3]

my_seq[::-1]

str(my_seq)

seq1 = Seq("ACGT")
seq2 = Seq("AACCGG")
seq1 + seq2

protein_seq = Seq("EVRNAK")
dna_seq = Seq("ACGT")
protein_seq + dna_seq

list_of_seqs = [Seq("ACGT"), Seq("AACC"), Seq("GGTT")]
concatenated = Seq("")
for s in list_of_seqs:
    concatenated += s
concatenated

spacer = Seq("N" * 10)
spacer.join(list_of_seqs)

dna = Seq("acgtACGT")
print(dna)
print("upper :", dna.upper()) #대문자로 변경
print("lower :", dna.lower()) #소문자로 변경

# 이는 대소문자를 구분하지 않고 일치를 한것을 찾는데 유용한다.
print("GTAC" in dna)
print("GTAC" in dna.upper())

# .complement() : 보체구하기
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(my_seq)
print(my_seq.complement())

# .reverse_complement() : 역보체
print(my_seq[::-1])
print(my_seq.reverse_complement())

# protein sequence
"""
단백질에 경우 IUPAC 모호성 코드에 의해 보완된다.
"""
print(protein_seq)
print(protein_seq.complement())

coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print(coding_dna)

template_dan = coding_dna.reverse_complement()
print(template_dan)

# .transcribe() : DNA -> RNA로
print(coding_dna)
mRNA = coding_dna.transcribe()
print(mRNA)

print(template_dan)
print(template_dan.transcribe())

# back_transcribe() : RNA -> DNA, 역전사
messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
print(messenger_rna)

print(messenger_rna.back_transcribe())

