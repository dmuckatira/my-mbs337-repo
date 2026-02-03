import json
from pydantic import BaseModel

#Make class blueprint of protein attributes
#I used ChatGPT here because i was very confused with how i would call the nested dictionaries in protein list
class ProteinEntry(BaseModel):
   primaryAccession: str
   organism: dict
   proteinName: str
   sequence: dict
   geneName: str
   function: str

with open('hw3.json', 'r') as f:
        prot_data = json.load(f)

proteins = []
for prot in prot_data["protein_list"]:
        proteins.append(ProteinEntry(**prot))

def find_total_mass(proteins):
    total_mass = 0 
    for p in proteins:
        total_mass = total_mass + p.sequence['mass']
    print(total_mass)


def find_large_proteins(proteins):
        large_proteins = []
        for p in proteins:
                if p.sequence['length'] >= 1000:
                        large_proteins.append(p.proteinName)
        return large_proteins
                
def find_non_eukaryotes(proteins):
    non_euk = []
    for p in proteins:
        if "Eukaryote" not in p.organism['lineage']:
                non_euk.append(p.proteinName)
        return non_euk


return find_total_mass(proteins)
return find_large_proteins(proteins)
return find_non_eukaryotes(proteins)



