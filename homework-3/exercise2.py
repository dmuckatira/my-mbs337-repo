import json
import csv

#Read json file and store it as prot_data
with open("hw3.json", "r") as f:
    prot_data = json.load(f)

with open("proteins.csv", "w") as o:
    csv_writer = csv.writer(o)

    # Make the column names
    header = [
        "primaryAccession",
        "proteinName",
        "geneName",
        "organism_scientificName",
        "sequence_length",
        "sequence_mass",
        "function"
    ]
    csv_writer.writerow(header)

    #Loop over the protein list and add the values
    for protein in prot_data["protein_list"]:
        row = [
            protein["primaryAccession"],
            protein["proteinName"],
            protein["geneName"],
            protein["organism"]["scientificName"],
            protein["sequence"]["length"],
            protein["sequence"]["mass"],
            protein["function"]
        ]
        csv_writer.writerow(row)