from sklearn.ensemble import RandomForestRegressor
import pandas as pd, numpy.random as rnd
import matplotlib, matplotlib.pyplot as plt

# 读取数据，准备两个随机的互补数据集
hed = pd.read_csv('Hedonic.csv')
selection = rnd.binomial(1, 0.7, size=len(hed)).astype(bool)
training = hed[selection]
testing = hed[-selection]

# 创建回归和预测集
rfr = RandomForestRegressor()
predictors_tra = training.ix[:, "crim":"lstat"]
predictors_tst = testing.ix[, "crim":"lstat"]

# 模型拟合
feature = "mv"
rfr.fit(predictors_tra, training[feature])

# 选择一种美观的样式
matplotlib.style.use("ggplot")

# 绘制预测结果
plt.scatter(training[feature], rfr.predict(predictors_tra), c="green", s=50)
plt.scatter(testing[feature], rfr.predict(predictors_tst), c="red")
plt.legend(["Training data", "Testing data"], loc="upper left")
plt.plot(training[feature], training[feature], c="blue")
plt.title("Hedonic Prices of Census Tracts in the Boston Area")
plt.xlabel("Actual value")
plt.ylabel("Predicted value")
plt.savefig("../images/rfr.pdf")