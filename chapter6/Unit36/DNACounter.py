import pandas as pd
dna = "AGTCCGCGAATACAGGCTCGGT"

dna1 = dna.replace("C", "")
dna2 = dna.replace("T", "")

dna_as_series1 = pd.Series(list(dna1), name="genes")
dna_as_series2 = pd.Series(list(dna2), name="genes")

print(dna_as_series1.value_counts() + dna_as_series2.value_counts())