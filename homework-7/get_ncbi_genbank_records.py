#!/usr/bin/env python3
from Bio import Entrez, SeqIO
import json
import redis
import argparse
import logging
import socket
import sys

# -------------------------
# Constants (configuration)
# -------------------------
output_file = 'output_files/genbank_records.txt'


# -------------------------
# Logging setup
# -------------------------
parser = argparse.ArgumentParser(
    description="Retrieve GenBank records from NCBI and store them in Redis"
)

parser.add_argument(
    '-l', '--loglevel',
    required=False,
    default='WARNING',
    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
    help='Set the logging level (default: WARNING)'
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

def search_ncbi(search_term: str = "Arabidopsis thaliana AND AT5G10140", retmax: int = 30) -> list:
    """
    Search the NCBI protein database and return a list of GI numbers.

    Args:
        search_term: The search string we are looking for in the NCBI database
            ("Arabidopsis thaliana AND AT5G10140").
        retmax: Maximum number of results to return (30).

    Returns:
        list: A list of GI number strings that match the search term.
    """
    Entrez.email = "A.N.Other@example.com"
    logging.info(f'Read through NCBI for {search_term}')
    with Entrez.esearch(db="protein", term=search_term, retmax=retmax) as h:
            results = Entrez.read(h)
            idlist = results["IdList"]
            logging.info(f'Found {len(idlist)} records')
            return idlist


def get_records(id_list: list) -> list:
    """
    Get GenBank records from NCBI for a list of GI numbers.

    Args:
        id_list: A list of GI number strings returned from search_ncbi().

    Returns:
        list: A list of SeqRecord objects containing the full GenBank records.
    """
    with Entrez.efetch(db="protein", id=",".join(id_list), rettype="gb", retmode="text") as h:
        record = SeqIO.parse(h, "gb")
        rec_list = list(record)
        logging.info(f'Got {len(rec_list)} records')
        return rec_list


def genbank_output(rec_list: list, output_file: str) -> None:
    """
    Connect to redis and get the values for the record ID's.

    Args:
        rec_list: A list of SeqRecord objects containing the full GenBank records.
        output_file: Path to the output txt file.

    Returns:
        None: This function does not return a value; it writes output to disk.
    """
    logging.info(f'Storing {len(rec_list)} records in Redis')
    rd = redis.Redis(host='127.0.0.1', port=6379, db=0)
    with open(output_file, 'w') as outfile:
        for record in rec_list:
            rd.set(record.id, json.dumps({
                "id": record.id,
                "name": record.name,
                "description": record.description,
                "sequence": str(record.seq)
            }))
            logging.info(f'writing to {output_file}')
            outfile.write(f'ID: {record.id}\n')
            outfile.write(f'Name: {record.name}\n')
            outfile.write(f'Description: {record.description}\n')
            outfile.write(f'Sequence: {str(record.seq)}\n')
            outfile.write('\n')

def main():
    logging.info(f'Starting record workflow')
    try:
        id_list = search_ncbi()
        rec_list = get_records(id_list)
        genbank_output(rec_list, args.output)
    except FileNotFoundError:
        logging.error(f'Output file {args.output} not found. Exiting.')
        sys.exit(1)
    logging.info(f'Record workflow complete')
    
if __name__ == '__main__':
    main()
