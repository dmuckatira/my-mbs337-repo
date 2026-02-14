from Bio.PDB.MMCIFParser import MMCIFParser
parser = MMCIFParser()

with open('4HHB.cif', 'r') as f:
    structure = parser.get_structure('myoglobin', f)


residues = 0
atoms = 0
for model in structure:
    for chain in model:
        #Get chain ID
        chain_id = chain.get_id()
        for residue in chain:
            #Get number of non-hetero residues
            if (residue.get_id()[0]) == " ":
                residues += 1
                for atom in residue:
                    #Get number of atoms in the non-hetero-residues in that chain
                    atoms += 1
        print(f'Chain {chain_id}: {residues} residues, {atoms} atoms') 
        residues = 0
        atoms = 0
