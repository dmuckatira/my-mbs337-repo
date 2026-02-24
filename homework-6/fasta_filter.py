#!/usr/bin/env python3
from Bio.SeqIO.FastaIO import SimpleFastaParser
import argparse
import logging
import socket
import sys

# -------------------------
# Constants 
# -------------------------

fasta_file = 'immune_proteins.fasta'
output_file = 'long_only.fasta'

# -------------------------
# Logging setup
# -------------------------
parser = argparse.ArgumentParser(
    description="Filter a FASTA file and write sequences >= a minimum length to a new FASTA file."
)

parser.add_argument(
    '-l', '--loglevel',
    required=False,
    default='WARNING',
    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
    help='Set log level to DEBUG, INFO, WARNING, ERROR, or CRITICAL (default: WARNING)'
)

parser.add_argument(
    '-i', '--input',
    required=True,
    type=str,
    default=fasta_file,
    help=f'Path to input FASTA file (default: {fasta_file})'
)

parser.add_argument(
    '-o', '--output',
    required=False,
    type=str,
    default=output_file,
    help=f'Path to output FASTA file (default: {output_file})'
)

parser.add_argument(
    '-m', '--minlen',
    required=False,
    type=int,
    default=1000,
    help='Minimum sequence length to keep (default: 1000)'
)

args = parser.parse_args()

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)
logging.basicConfig(level=args.loglevel, format=format_str)




# -------------------------
# Functions
# -------------------------

def long_fasta(fasta_file: str, output_file: str, min_len: int) -> None:
    """
    Given a single FASTA record, extract sequences larger than 1000 residues

    Args:
        fasta_file: Path to fasta input file
        output_file: Path to fasta output file

    Returns:
        None: Writes output to disk
    """
    logging.info(f"Reading FASTA file: {fasta_file}")
    #Reads certain file
    with open(fasta_file, 'r') as f, open(output_file, 'w') as of:
        #Saves specific fasta file with both outputs
        for header, sequence in SimpleFastaParser(f):
            #Grab the sequences
            #See if the sequence is  > 1000 
            if len(sequence) > min_len:
                logging.info(f"Writing output to: {output_file}")
                #Write out the header and sequence
                of.write(f">{header}\n")
                of.write(f"{sequence}\n")


def main():
    logging.info("Starting FASTA filter workflow")

    try:
        long_fasta(args.input, args.output, args.minlen)

    except FileNotFoundError:
        logging.error(f"Input FASTA file '{args.input}' not found. Exiting.")
        sys.exit(1)

    logging.info("FASTA filter workflow complete")

if __name__ == '__main__':
    main()


        
    
