import pandas as pd

alco2009 = pd.DataFrame([(1.20, 0.22, 0.58),
                         (1.31, 0.54, 1.16),
                         (1.19, 0.38, 0.74)]
                        , columns=("Beer", "Wine", "Spirits"),
                        index=("Alabama", "Alaska", "Arizona"))
alco2009["Total"] = alco2009.Wine + alco2009.Beer + alco2009.Spirits
print(alco2009)
