from Bio.Seq import Seq

dna_seq = Seq("GAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAA")
#function
def base_func(dna):
    #dictionary
    seq_dict = {
    #base pair count
    'A' : 100 * dna.count('A') / len(dna),
    'T' : 100 * dna.count('T') / len(dna),
    'G' : 100 * dna.count('G') / len(dna),
    'C' : 100 * dna.count('C') / len(dna),
    }
    return seq_dict

result = base_func(dna_seq)
for base, percent in result.items():
    print(f"{base}: {percent:.2f}%")