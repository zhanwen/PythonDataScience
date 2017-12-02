import pandas as pd
import numpy as np

# 最后的值是错误的，我们稍后在修改它
inflation = pd.Series((2.2, 3.4, 2.8, 1.6, 2.3, 2.7, 3.4, 3.2, 2.8, 3.8, -0.4, 1.6, 3.2, 2.1, 1.5, 1.5))

# print(len(inflation))
#
# print(inflation.index.values)
#
# print(inflation.values)

inflation.values[-1] = 1.6

# inflation = pd.Series({1999 : 2.2, 2004 : 1.6, 2015 : np.nan})
# print(inflation)
inflation.index = pd.Index(range(1999, 2015))
inflation[2015] = np.nan
# print(inflation)

inflation.index.name = "Year"
inflation.name = "%"

# 输出 inflation 的前五行，可以自行指定具体的行数
print(inflation.head())
# 输出 inflation 的后五行，可以自行指定具体的行数
print(inflation.tail())