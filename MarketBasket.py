import pandas as pd
import numpy as np

#数据加载 不知道什么原因导致相对路径不好使，读取不到文件，只能用绝对路径读取，影响不大
dataset = pd.read_csv('c:/Users/Dracula/Desktop/开课吧作业/HXHomeWork2/Market_Basket_Optimisation.csv',header=None)
# print(dataset.head())
# print(dataset.shape[0])

#把数据存放到transaction中
transaction = []
for i in range(0,dataset.shape[0]):
    temp = []
    for j in range(0,dataset.shape[1]):
        #数据预处理，将nan过滤掉并且将内容全部小写以避免因大小写而产生的分组问题
        if str(dataset.values[i,j]) !='nan' : 
            temp.append(str(dataset.values[i,j]).lower())
    transaction.append(temp)

# print(transaction)

#导包，简版apriori算法求出频繁项集，关联规则
def efficient_apriori_func():
    from efficient_apriori import apriori
    itemsets , rules = apriori(transaction,min_support=0.02,min_confidence=0.3)
    print('频繁项集:',itemsets)
    print('关联规则:',rules) 

def mlxtend_appriori_func():
    from mlxtend.frequent_patterns import apriori
    from mlxtend.frequent_patterns import association_rules
    pd.options.display.max_columns=100

# mlxtend_appriori_func()
efficient_apriori_func()






