#!/usr/bin/env python3
from Bio.SeqIO.FastaIO import SimpleFastaParser
import argparse
import logging
import socket
import sys

# -------------------------
# Constants (configuration)
# -------------------------

fasta_file = 'immune_proteins.fasta'
output_file = 'immune_proteins_stats.txt'

# -------------------------
# Logging setup
# -------------------------
parser = argparse.ArgumentParser(
    description="Summarize FASTA file and write residue stats to a text file"
)

parser.add_argument(
    '-l', '--loglevel',
    required=False,
    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
    default='WARNING',
    help='Set the logging level (default: WARNING)'
)

parser.add_argument(
    '-i', '--input',
    required=True,
    type=str,
    default=fasta_file,
    help=f'Input FASTA file (default: {fasta_file})'
)

parser.add_argument(
    '-o', '--output',
    required=False,
    type=str,
    default=output_file,
    help=f'Output text file (default: {output_file})'
)

args = parser.parse_args()

format_string = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(module)s.%(funcName)s:%(lineno)s - %(levelname)s - %(message)s'
)

logging.basicConfig(level=args.loglevel, format=format_string)


# -------------------------
# Functions
# -------------------------


def residue_count(fasta_file: str, output_file: str) -> None:
    """
    Given a single FASTA record, extract sequence and residue statistics, and
    return them as a .txt instance

    Args:
        fasta_file: Path to fasta file
        output_file: Path to txt file

    Returns:
        None: Writes output to disk
    """
    logging.info(f"Reading FASTA file: {fasta_file}")

    #Reads certain file
    with open(fasta_file, 'r') as f, open(output_file, 'w') as outfile:
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

        logging.info(f"Writing output to: {output_file}")
        #Print outputs
        outfile.write(f'Num Sequences: {count} \n')
        #Print Residues
        outfile.write(f'Total Residues: {residues} \n')
        #print(accession)
        outfile.write(f'Longest Accession: {longest_seq_id} ({longest_seq_length} residues) \n')
        outfile.write(f'Shortest Accession: {shortest_seq_id} ({shortest_seq_length} residues) \n')

def main():
    logging.info("Starting FASTA sequence summary workflow")

    try:
        residue_count(args.input, args.output)

    except FileNotFoundError:
        logging.error(f"Input FASTA file '{fasta_file}' not found. Exiting.")
        sys.exit(1)

    logging.info("FASTA sequence summary workflow complete")

if __name__ == '__main__':
    main()
    
    