import pandas as pd
dna = "AGTCCGCGAATACAGGCTCGGT"

dna_as_series = pd.Series(list(dna), name="genes")
print(dna_as_series.head())

print(dna_as_series.unique())

print(dna_as_series.value_counts().sort_index())
print(dna_as_series.value_counts())

valid_nucs = list("ACGT")
print(dna_as_series.isin(valid_nucs).all())
