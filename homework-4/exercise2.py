from Bio.SeqIO.FastaIO import SimpleFastaParser
#Reads certain file
with open('immune_proteins.fasta', 'r') as f, open('long_only.fasta', 'w') as of:
    #Saves specific fasta file with both outputs
    for header, sequence in SimpleFastaParser(f):
        #Grab the sequences
        #See if the sequence is  > 1000 
        if len(sequence) > 1000:
            #Write out the header and sequence
            of.write(f">{header}\n")
            of.write(f"{sequence}\n")
        
        
    
