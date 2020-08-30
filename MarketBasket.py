import pandas as pd
import numpy as np

#数据加载 不知道什么原因导致相对路径不好使，读取不到文件，只能用绝对路径读取影响不大
dataset = pd.read_csv('c:/Users/Dracula/Desktop/开课吧作业/HXHomeWork2/Market_Basket_Optimisation.csv',header=None)
print(dataset.head())
print(dataset.shape[0])

#把数据存放到transaction中
transaction = []
for i in range(0,dataset.shape[0]):
    


