import pandas as pd

alco2009 = pd.DataFrame([(1.20, 0.22, 0.58),
                         (1.31, 0.54, 1.16),
                         (1.19, 0.38, 0.74)]
                        , columns=("Beer", "Wine", "Spirits"),
                        index=("Alabama", "Alaska", "Arizona"))

# print(alco2009)
#
# print(alco2009["Wine"].head())

# print(alco2009.Beer.tail())

alco2009["Total"] = 0
print(alco2009.head())