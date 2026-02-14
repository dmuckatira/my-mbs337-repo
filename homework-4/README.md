# Homework 4

Simple overview of use/purpose.

## Setup Instructions

I ran these exercises in a virtual environment with the **pydantic** and **biopython** packages installed:
```bash
source myenv/bin/activate
pip3 install pydantic
pip3 install biopython
```

## Exercise Descriptions

### Exercise 1
***Requires pydantic package***
***Requires SimpleFastaParser from Bio.SeqIO.FastaIO***

Description of the exercise and what you did. Optionally describe any functions/classes defined within your code:
1. **The total number of sequences in the file**: I used SimpleFastaParser to iterate through each sequence in the FASTA file and incremented a counter every time the loop ran, which gave me the total number of sequences.
2. **The total number of residues in the file**: For each sequence, I calculated its length using len(sequence) and continuously added it to a running total to compute the total number of residues across all proteins.
3. **The accession ID and length of the longest sequence in the file**: During iteration, I compared each sequence length to the current longest length and updated the stored accession ID and length whenever a longer sequence was found.
4. **The accession ID and length of the shortest sequence in the file**: Similarly, I tracked the shortest sequence by comparing each sequence length to a predefined large starting value and updating the accession ID and length whenever a shorter sequence appeared.

## Note on AI Usage (if applicable)


### Exercise 2
***Requires SimpleFastaParser from Bio.SeqIO.FastaIO***

1. **Write out a new FASTA file called long_only.fasta containing only the sequences longer than or equal to 1000 residues**: Using SimpleFastaParser, I looped through each (header, sequence) pair in the original FASTA file. Inside the loop, I checked len(sequence) and, if it was greater than 1000, wrote the formatted header and sequence to a new file (long_only.fasta) using of.write().

### Exercise 3
***Requires Bio import from Bio.SeqIO.FastaIO***

1. **Print total reads in original file**: I used SeqIO.parse() to iterate through each FASTQ record and incremented read_count during every loop iteration, which gives the total number of reads in the file.
2. **Print read count with an average Phred quality is at least 30**: For each record, I accessed record.letter_annotations['phred_quality'], calculated the average score, and incremented new_reads_count if the average was ≥ 30.
3. **Write out filtered reads out to a new FASTQ file named sample1_cleanReads.fastq**: Inside the same quality check, I used SeqIO.write(record, of, "fastq-sanger") to write only the reads passing the ≥ 30 threshold to sample1_cleanReads.fastq.

### Exercise 4
***Requires MMCIFParser import from Bio.PDB.MMCIFParser***

1. **Iterates over the full structure hierarchy of a mmCIF summary and for each chain, print: Chain ID, Number of non-hetero-residues in that chain, Number of atoms in the non-hetero-residues in that chain**: I used MMCIFParser() to load the mmCIF structure and then iterated through the full hierarchy (model → chain → residue → atom). For each chain, I checked residue.get_id()[0] == " " to count only non-hetero residues, incremented a residue counter, and then counted all atoms within those residues before printing the chain ID, residue count, and atom coun

Describe which/how AI tools were used to complete your homework exercises.