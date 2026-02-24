import json
import yaml

#reads uniprot list and stores the data
with open("uniprot_protein_list.json", "r") as f:
    prot_data = json.load(f)

#writes out the file in correct format
with open("proteins.yaml", "w") as o:
    yaml.dump(
        prot_data,
        o,
        #sorts keys 
        sort_keys=False,    
        #adds ---    
        explicit_start=True,    
        #adds ...
        explicit_end=True       
    )