from Bio.SeqRecord import SeqRecord
help(SeqRecord)

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

simple_seq = Seq("GATC")
simple_seq_r = SeqRecord(simple_seq)

simple_seq_r.id

simple_seq_r.id = "AC12345"
simple_seq_r.description = "Made up sequence I wish I could write a paper about"
print(simple_seq_r.description)

simple_seq_r.id

simple_seq_r.seq

