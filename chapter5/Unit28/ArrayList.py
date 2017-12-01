import numpy as np

sap = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"])

dna = "AGTCCGCGAATACAGGCTCGGT"

dna_as_array = np.array(list(dna))

result = np.unique(dna_as_array)

cha = np.in1d(["MSFT", "MMM", "AAPL"], sap)

print(np.union1d(["MSFT", "MMM", "AAPL"], sap))

print(np.intersect1d(["MSFT", "MMM", "AAPL"], sap))

