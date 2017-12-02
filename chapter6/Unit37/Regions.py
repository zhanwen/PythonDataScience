import pandas as pd

regions = pd.read_csv("data/regions.csv", header=None, names={"region", "division", "state"})

state2reg_series = regions.ffill().set_index("state")["region"]
# print(state2reg_series.head())

regions.to_csv("data/regions_clean.csv")