import numpy as np

sap = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"])

np.save("sap.npy", sap)

sap_copy = np.load("sap")

fname = "sap.npy"
arr = np.loadtxt(fname, comments="#", delimiter=None, skiprows=0)

np.savetxt(fname, arr, comments='#', delimiter=" ", dtype=float)