from Bio import SeqIO

with open('sample1_rawReads.fastq', 'r') as f, open('sample1_cleanReads.fastq', 'w') as of:
    
    #Make a count of how many reads in total. Make an empty list to store sequences
    read_count = 0
    new_reads_count = 0
    #Record will return 4 lines of fastq
    for record in SeqIO.parse(f, 'fastq-sanger'):
        #Get average phred quality 
        phred_scores = record.letter_annotations['phred_quality']
        average_phred = sum(phred_scores) / len(phred_scores)

        #Condition avg phred quality so if >30 append it to the list 
        ### How do I add to list so it looks good in fastq
        if average_phred >= 30:
            SeqIO.write(record, of, "fastq-sanger")
            new_reads_count += 1
        #Add to count after each iteration
        read_count += 1



    
    print(f'Total reads in original file: {read_count}')
    print(f'Reads passing filter: {new_reads_count}')