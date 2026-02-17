# Homework 5

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
***Requires json package***
***Requires pydantic package***
***Requires MMCIFParser from Bio.PDB.MMCIFParser***
***Requires import argparse***
***Requires import logging***
***Requires import socket***
***Requires import sys***

Description of the code and functions and what it does. 
1. **classChainSummary and classCifSummary**: These are Pydantic data models used to define the structure of the output JSON file. ChainSummary stores per-chain statistics including the chain ID, total residues, number of standard (non-hetero) residues, and number of hetero residues. CifSummary contains a list of ChainSummary objects and represents the full mmCIF summary structure written to JSON.
2. **summarize_myoglobin()**: This function takes a single chain from the parsed mmCIF structure and finds residue counts for that chain. It iterates through every residue, increments a counter for the total number of residues, and checks whether each residue is a standard residue by examining its residue ID. It then calculates the hetero residue count by subtracting total residues and standard residues and returns a ChainSummary containing the chain ID and all computed values.
3. **summarize_cif_file()**: This function reads the mmCIF file using MMCIFParser, extracts the first model, and iterates over all chains in that model. For each chain, it calls summarize_myoglobin() to count the residues and appends the results to a list. It then returns a CifSummary object containing summaries for all chains in the structure.
4. **write_summary_to_json()**: This function takes a CifSummary object and writes it into JSON format using model_dump(). The result is written to a JSON output file.
5. **def main()**: This function runs the whole code and includes a try/except code to handle missing input files and logs an error if the file cannot be found.

**ChatGPT was used to when making the classes in order to distinguish the chain list from the chain content for each function**