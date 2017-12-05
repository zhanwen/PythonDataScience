import numpy.random as rnd

#使用numpy来创建数据

r1 = rnd.uniform(low=0.0, high=1.0, size=None)
print(r1)

# rnd.rand(shape)  相当于uniform(0.0, 1.0, None)
# r2 = rnd.randint(low=None, high=None, size=None)
r3 = rnd.normal(loc=0.0, scale=1.0, size=None)
print(r3)

# rnd.randn(shape) 等同于normal(0.0, 1.0, shape)
# rnd.binomial(n, p, size=None)


