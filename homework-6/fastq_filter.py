#!/usr/bin/env python3
from Bio import SeqIO
import argparse
import logging
import socket
import sys

# -------------------------
# Constants (configuration)
# -------------------------

fastq_file = 'sample1_rawReads.fastq'
output_file = 'sample1_cleanReads.fastq'


# -------------------------
# Logging setup
# -------------------------
parser = argparse.ArgumentParser(
    description="Filter a FASTQ file and write sequences >= a minimum phred quality to a new FASTQ file."
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
    default=fastq_file,
    help=f'Path to input FASTQ file (default: {fastq_file})'
)

parser.add_argument(
    '-o', '--output',
    required=False,
    type=str,
    default=output_file,
    help=f'Path to output FASTQ file (default: {output_file})'
)

parser.add_argument(
    '-e', '--encoding',
    choices=['fastq-sanger', 'fastq-solexa', 'fastq-illumina'],
    default='fastq-sanger',
    help='The FASTQ encoding format (default: fastq-sanger)'
)

parser.add_argument(
    '-m', '--minphred',
    required=False,
    type=int,
    default=30,
    help='Minimum phred quality to keep (default: 30)'
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

def long_fasta(fastq_file: str, output_file: str, encoding: str, min_phred: int) -> None:
    """
    Given a single FASTQ record, extract sequences with a Phred quality >= 30

    Args:
        fastq_file: Path to fastq input file
        output_file: Path to fastq output file

    Returns:
        None: Writes output to disk
    """
    logging.info(f"Reading FASTQ file: {fastq_file}")
    with open(fastq_file, 'r') as f, open(output_file, 'w') as of:
    
        #Make a count of how many reads in total. Make an empty list to store sequences
        read_count = 0
        new_reads_count = 0
        #Record will return 4 lines of fastq
        for record in SeqIO.parse(f, encoding):
            #Get average phred quality 
            phred_scores = record.letter_annotations['phred_quality']
            average_phred = sum(phred_scores) / len(phred_scores)

            #Condition avg phred quality so if >30 append it to the list 
            ### How do I add to list so it looks good in fastq
            if average_phred >= min_phred:
                SeqIO.write(record, of, encoding)
                new_reads_count += 1
            #Add to count after each iteration
            read_count += 1
        
def main():
    logging.info("Starting FASTQ filter workflow")

    try:
        long_fasta(args.input, args.output, args.encoding, args.minphred)

    except FileNotFoundError:
        logging.error(f"Input FASTQ file '{args.input}' not found. Exiting.")
        sys.exit(1)

    logging.info("FASTQ filter workflow complete")

if __name__ == '__main__':
    main()