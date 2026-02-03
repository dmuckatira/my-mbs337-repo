import json
import yaml

with open("uniprot_protein_list.json", "r") as f:
    prot_data = json.load(f)

with open("proteins.yaml", "w") as o:
    yaml.dump(
        prot_data,
        o,
        sort_keys=False,        
        explicit_start=True,    
        explicit_end=True       
    )