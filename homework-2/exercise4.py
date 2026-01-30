#Create nested dictionary of genes. Used nested so I can hole more than 1 with multiple values
RNA_dict = {
    "Gene 1" : {
        "control" : [10.5, 11.2, 10.8],
        "treatment"  : [25.3, 24.7, 26.1]
    },

    "Gene 2" : {
        "control" : [8.2, 8.5, 8.0], 
        "treatment" : [12.1, 11.8, 12.5]
    },

    "Gene 3" : {
        "control" : [15.0, 14.8, 15.2], 
        "treatment" : [18.5, 18.2, 18.8]
    }

}
#Loop over dictrionary and output values
for gene in RNA_dict:
    control_vals = RNA_dict[gene]["control"]
    treatment_vals = RNA_dict[gene]["treatment"]

    control_mean = sum(control_vals) / len(control_vals)
    treatment_mean = sum(treatment_vals) / len(treatment_vals)

    fold_change = treatment_mean / control_mean
    #Test significance
    if fold_change > 2.0 or fold_change < 0.5:
        sig = "significant"
    else:
        sig = "not significant"

    print(f"{gene}: Control={control_mean:.2f}, Treatment={treatment_mean:.2f}, "
          f"FoldChange={fold_change:.2f} → {sig}")