import numpy as np

# 几个标准的普尔 （S&P）股票代码
sap = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"])
# print(sap)

sap2d = sap.reshape(2, 4)
print(sap2d)

sap3d = sap.reshape(2, 2, 2)
# print(sap3d)

print(sap2d.T)

print(sap2d.swapaxes(0, 1))

print(sap3d.transpose((0, 2, 1)))