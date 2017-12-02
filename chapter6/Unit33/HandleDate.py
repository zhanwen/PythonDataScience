import pandas as pd
import numpy as np
alco2009 = pd.DataFrame([(1.20, 0.22, 0.58),
                         (1.31, 0.54, 1.16),
                         ]
                        , columns=("Beer", "Wine", "Spirits"),
                        index=("South Carolina", "South Dakota"))
alco2009.index.name = "State"

s_stats = [state for state in alco2009.index if state[0] == 'S'] + ["Samoa"]
drinks = list(alco2009.columns) + ["Water"]
nan_alco = alco2009.reindex(s_stats, columns=drinks)

# print(alco2009.dropna(how="all"))
# print(alco2009.dropna(how="all", axis=1))
# print(alco2009.dropna())

# print(nan_alco.isnull())
# print(nan_alco.notnull())

# 选中具有'脏'值的一列数据
sp = nan_alco['Spirits']
# '干净'值的编号
clean = sp.notnull()
# 使用平均值来修正'脏'值
sp[-clean] = sp[clean].mean()
# print(nan_alco)

nan_alco.fillna(0)

nan_alco.fillna(method="ffill")
print(nan_alco)