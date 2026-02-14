from Bio.SeqIO.FastaIO import SimpleFastaParser
#Reads certain file
with open('immune_proteins.fasta', 'r') as f:
    #We need to save fasta file 
    #SimpleFastaParser returns 2 things: header and sequence
    #iterate over entire file with for loop
    #count is just how many times this for loop runs aka how many sequences there are
    #residues is a new counter for residues
    count = 0
    residues = 0
    longest_seq_id = ""
    longest_seq_length = 0
    shortest_seq_id = ""
    shortest_seq_length = 10000000000000

    for header, sequence in SimpleFastaParser(f):
        # The total number of sequences in the file
        count += 1
        # Grab the accession ID as a list of items in the header
        parts = header.split('|')
        #We need the [1] index of the header for the accession ID
        accession = parts[1]
        #I need to iterate each protein sequence and count each individual residue and add it to the counter
        residues += len(sequence)

        #Now take each new residue and compare it to longest_seq_length and keep whichever one is biggest
        if len(sequence) > longest_seq_length:

            # Grab the accession ID as a list of items in the header
            parts = header.split('|')
            #We need the [1] index of the header for the accession ID
            accession = parts[1]

            #Saves longest seq id
            longest_seq_id = accession
            #Save longest seq length as new number
            longest_seq_length = len(sequence)

        #Do the same for the short sequence
        
        if len(sequence) < shortest_seq_length:
            # Grab the accession ID as a list of items in the header
            parts = header.split('|')
            #We need the [1] index of the header for the accession ID
            accession = parts[1]

            #Saves shortest seq id
            shortest_seq_id = accession
            #Save shortest seq length as new number
            shortest_seq_length = len(sequence)




    #Print outputs
    print(f'Num Sequences: {count}')
    #Print Residues
    print(f'Total Residues: {residues}')
    #print(accession)
    print(f'Longest Accession: {longest_seq_id} ({longest_seq_length} residues)')
    print(f'Shortest Accession: {shortest_seq_id} ({shortest_seq_length} residues)')
    
    