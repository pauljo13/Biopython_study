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