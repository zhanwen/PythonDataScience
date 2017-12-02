import pandas as pd

chunker = pd.read_csv("data/regions_clean.csv", chunksize=5, header=None, names=("region", "division", "state"))

accum = pd.Series()

for piece in chunker:
    counts = piece["region"].value_counts()
    accum = accum.add(counts, fill_value=0)

print(accum)