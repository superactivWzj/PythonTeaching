import pandas as pd
import numpy as np

# 用值构建一个Series：由默认index和values组成
# series1 = pd.Series(np.random.randn(4))
# print("add 1 before")
# print(series1)
#
#
# def add_one(x, y):
#     return x + y
#
#
# print(type(add_one))
# f_np = np.frompyfunc(add_one, 2, 1)
# print("add 1 after")
# print(f_np(series1, series1))

df = pd.read_csv('/Users/weizijian/Downloads/PythonTeaching/new_data.txt', header=None, sep=',',
                 names=["date", "confirm", "cured", "death"])
print(df)
df.set_index(["date"], inplace=True)
# print(df.values)
# print(df.index)
print(df.describe())
