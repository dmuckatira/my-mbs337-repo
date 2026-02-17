import json
from Bio.PDB.MMCIFParser import MMCIFParser
from pydantic import BaseModel
import argparse
import logging
import socket
import sys


#Classes
#I used my friend who is a CS major and ChatGPT to help me reason through and make the class because I had no idea I was supposed to use 
#2 different classes for each function. I thought I could add the chains: part of the JSON into the classChainSummary but I needed to keep it separate since
#each function returns a different part of the JSON and then later combines them
class ChainSummary(BaseModel):
    chain_id: str
    total_residues: int
    standard_residues: int
    hetero_residue_count: int

class CifSummary(BaseModel):
    chains: list[ChainSummary]

#Logging Setup
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--loglevel',
                    type=str,
                    required=False,
                    default='WARNING',
                    help='set log level to DEBUG, INFO, WARNING, ERROR, or CRITICAL')
args = parser.parse_args()

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)
logging.basicConfig(level=args.loglevel, format=format_str)


#Constants
cif_file = '4HHB.cif'
output_json = '4HHB_summary.json'
parser = MMCIFParser()

#JSON class function
def summarize_myoglobin(chain: object) -> ChainSummary:
    """
    Given a single mmCIF chain, find the different residue counts and
    return them as a ChainSummary instance

    Args:
        chain: A chain of the myoglobin produced by Bioython's MMCIFParse, 
            containing the total residues, hetero residue, and standard residues.

    Returns:
        ChainSummary: A ChainSummary instance containing chain id and the number of 
            total residues, hetero residue, and standard residues.
    """

    #Start residue count
    total_residues = 0
    nonhetero_residues = 0
    hetero_residues = 0

    #Iterate over chains to get residue count
    chain_id = chain.get_id()
    logging.debug(f"Summarizing chain {chain_id}")
    for residue in chain:
        total_residues += 1
        #Get number of non-hetero residues
        if (residue.get_id()[0]) == " ":
            nonhetero_residues += 1
    hetero_residues = total_residues - nonhetero_residues
    logging.info(f'Finished reading {chain_id} residues')

    return ChainSummary(
        chain_id= chain_id,
        total_residues= total_residues,
        standard_residues= nonhetero_residues,
        hetero_residue_count= hetero_residues
    )
   


#read and summarize function
def summarize_cif_file(cif_file: string) -> CifSummary:
    """
    Given as mmCIF file, this function iterates over each chain's resides in the file,
    gets the count of each type of residue, and returns the results as a ChainSummary instance.

    Args:
        cif_file: Path to the input mmCIF file.

    Returns:
        CifSummary: A CifSummary instance containing the chain id and the number of 
            total residues, hetero residue, and standard residues of the mmCIF input file.
    """
    chain_list = []
    logging.info(f'Reading mmCIF file {cif_file}')
    with open(cif_file, 'r') as f:
        structure = parser.get_structure('myoglobin', f)
    #mmCIF structures contains multiple models, only itereate through the first model
    first_model = structure[0]
    for chain in first_model:
        chain_list.append(summarize_myoglobin(chain))              
    return CifSummary(chains=chain_list)

#save file and loop
def write_summary_to_json(summary: CifSummary, output_file: str) -> None:
    """
    Given a CifSummary instance, serialize the data and write it to a JSON file.

    Args:
        summary: A CifSummary object containing a chain's id and residue data.
        output_file: Path to the output JSON file.

    Returns:
        None: This function does not return a value; it writes output to disk.
    """
    with open(output_file, 'w') as outfile:
        json.dump(summary.model_dump(), outfile, indent=2)



def main():
    logging.info(f'Starting summary workflow')
    try:
        summary = summarize_cif_file(cif_file)
        write_summary_to_json(summary, output_json)
        logging.info(f'mmCIF summary workflow complete!')

    except FileNotFoundError:
        logging.error(f"Input mmCIF file {cif_file} not found. Exiting.")
        sys.exit(1) # Stop the execution of the script with an error



if __name__ == '__main__':
    main()




