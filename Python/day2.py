from Bio.Seq import Seq
m_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
m_rna

m_rna.translate()

coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
coding_dna

coding_dna.translate()

# 번역은 NCBI의 변환표를 기반으로 만들어졌다.
coding_dna.translate(table="Vertebrate Mitochondrial")

# NCBI 테이블 번호를 사용하여 테이블을 지정할 수 있다.
coding_dna.translate(table=2)

coding_dna.translate()

# 정지 코돈의 첫 번째까지 번역하게 할 수 있다.
# 종료 코돈 자체를 번역하지 않는다.
coding_dna.translate(to_stop=True)

coding_dna.translate(table=2)

coding_dna.translate(table=2, to_stop=True)

# stop_symbol로 종료 코돈을 표시할 수 있다.
coding_dna.translate(table=2, stop_symbol="@")

gene = Seq(
    "GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCA"
    "GCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGAT"
    "AATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACAT"
    "TATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCAT"
    "AAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA"
)
print(gene)
gene.translate(table="Bacterial")

gene.translate(table="Bacterial", to_stop=True)

gene.translate(table="Bacterial", cds=True)
"""박테리아 유전 코드에는 GTG 유효한 시작코돈이 있으나, 일반적으로 메티오닌으로 번역되는데 cds를 이용해 메티오닌으로 번역되도록 한다."""


from Bio.Data import CodonTable
standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
# or = CodonTable.unambiguous_dna_by_id[1]
mito_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
# or = CodonTable.unambiguous_dna_by_id[2]

print(standard_table)

print(mito_table)

# 직접 유전자 코드를 입력하거나 메서드로 유전코드를 검색할 수 있다.
mito_table.start_codons

mito_table.stop_codons

mito_table.forward_table["ACG"]

seq1 = Seq("ACGT")
"ACGT" == seq1

seq1 == "ACGT"

unknown_seq = Seq(None, 10)
unknown_seq

len(unknown_seq)

print(unknown_seq)

seq = Seq({117512683: "TTGAAAACCTGAATGTGAGAGTCAGTCAAGGATAGT"}, length=159345973)
seq

seq[1000:1020]

seq[117512690:117512700]

seq[117512670:117512690]

seq[117512700:]

seq = Seq("ACGT")
undefined_seq = Seq(None, length=10)
seq + undefined_seq + seq

my_seq = Seq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")

my_seq[5]

# seq는 읽기 전용으로 수정할 수 없다.
my_seq[5] = "G"

from Bio.Seq import MutableSeq

# MutableSeq으로 시퀀스 서열을 수정할 수 있다.
mutable_seq = MutableSeq(my_seq)
mutable_seq

mutable_seq = MutableSeq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
print(mutable_seq)


print(mutable_seq[5])
mutable_seq[5] = "C"
print(mutable_seq[5])
print(mutable_seq)

# T 을 제거
mutable_seq.remove("T")
mutable_seq

# 순서를 반대로 만들기
mutable_seq.reverse()
mutable_seq

# 편집 후 다시 읽기 전용으로 변경할 수 있다.
new_seq = Seq(mutable_seq)
new_seq

seq = Seq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
seq.index("ATGGGCCGC")

seq.index(b"ATGGGCCGC")

seq.index(bytearray(b"ATGGGCCGC"))

seq.index(Seq("ATGGGCCGC"))

seq.index(MutableSeq("ATGGGCCGC"))

seq.index("ACTG")

seq.find("ACTG")
# 발견되지 않으면 -1 을 반환

seq.find("CC")

# 오르쪽에서부터 시작하여 검색
seq.rfind("CC")

for index, sub in seq.search(["CC", "GGG", "CC"]):
    print(index, sub)

from Bio.Seq import reverse_complement, transcribe, back_transcribe, translate
my_string = "GCTGTTATGGGTCGTTGGAAGGGTGGTCGTGCTGCTGGTTAG"

reverse_complement(my_string)

transcribe(my_string)

back_transcribe(my_string)

translate(my_string)