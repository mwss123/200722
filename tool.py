# Teacher

import sys

class FASTA :
    def __init__(self, file_name : str) :
        self.file_name = file_name
        self.count = {}
        self.length = 0

    def count_base(self) :
        with open (self.file_name, 'r') as f1 :
            for line in f1 :
                if line.startswith(">")  :
                    continue
                line = line.strip()
                for s in line :
                    if s in self.count :
                        self.count[s] += 1
                    else :
                        self.count[s] = 1


    def __len__(self) :
        for k, v in self.count.items() :
            self.length += v
                                         # python  basic hamsu, juck-young dae do rok.
        return self.length



class FASTQ :
    def __init__(self,filename : str) :
        self.filename = filename
        self.read_num = 0
	#self.base = {}

    def count_read_num(self) :
        cnt = 0
        with open(self.filename, 'r') as f1 :
            for line in f1 :
                if cnt % 4 == 0 :
                    header = line.strip()
                    self.read_num += 1
                elif cnt % 4 == 1 :
                    seq = line.strip()
                    for s in seq :
			if s in self.base :
			    self.base[s] += 1
			else :
			    self.base[s] = 1
		elif cnt % 4 == 3 :
		    qual = line.strip()
		cnt += 1
	


if __name__ == '__main__' :
    if len(sys.argv) != 2 :
        print(f"usage : python {sys.argv[0]} [fasta]")
        sys.exit()

    filename = sys.argv[1]
    t = FASTQ(filename)
    t.count_read_num()
    print(t.read_num)


"""
    file_name = sys.argv[1]
    t = FASTA(file_name)
    t.count_base()
    print(t.count)
    t.get_length()
    print(t.length)
"""
