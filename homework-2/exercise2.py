from Bio.Seq import Seq

dna_seq = Seq("GAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAA")
G_cont = dna_seq.count("G") 
C_cont = dna_seq.count("C")
GC_cont = G_cont + C_cont
print("GC content = " + str(GC_cont) + " or " + str(100 * (GC_cont)/len(dna_seq)) + "%")
