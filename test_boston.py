from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression  # 线性回归
from sklearn.linear_model import SGDRegressor  # 快速随机梯队下降(Stochastic Gradient Descend)
# 这个R评价方式考量回归值和真实值的差异，也兼顾了问题本身真实值的变动
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# 加载房价数据
boston = load_boston()  # 共506条数据
X = boston.data
y = boston.target

# 训练数据和测试数据分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

# 标准化
ss_X = StandardScaler()
ss_y = StandardScaler()

X_train = ss_X.fit_transform(X_train)
X_test = ss_X.transform(X_test)
y_train = ss_y.fit_transform(y_train.reshape(-1, 1))
y_test = ss_y.transform(y_test.reshape(-1, 1))

# 用线性回归模型中的LinearRegression和SGDRegression进行预测
# 这个是正规的方程来求解
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_y_predict = lr.predict(X_test)
# SGDRegression，这个也就是随机梯度下降进行线性回归预测
# 小样本随机梯度下降不咋地，但是训练数据大的话这个就高效很多了，能节省很多时间的
sgdr = SGDRegressor()
sgdr.fit(X_train, y_train)
sgdr_y_predict = sgdr.predict(X_test)

# 评价
print('The scroe of LinearRegression is:', lr.score(X_test, y_test))
print('The r2-score of LinearRegression is:', r2_score(y_test, lr_y_predict))
print('The mean_squared_error of LinearRegression is',
      mean_squared_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(lr_y_predict)))
print('The mean_absolute_error of LinearRegression is',
      mean_absolute_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(lr_y_predict)))

# 评价
print('The scroe of SGDRegression is:', sgdr.score(X_test, y_test))
print('The r2-score of SGDRegression is:', r2_score(y_test, sgdr_y_predict))
print('The mean_squared_error of SGDRegression is',
      mean_squared_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(sgdr_y_predict)))
print('The mean_absolute_error of SGDRegression is',
      mean_absolute_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(sgdr_y_predict)))
