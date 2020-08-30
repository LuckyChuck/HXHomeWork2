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
    print('频繁项集大小:',len(itemsets[1])+len(itemsets[2]))
    print('关联规则:',rules) 
    print('关联规则大小:',len(rules)) 

#导包，详细版mlxtend
def mlxtend_appriori_func():
    from mlxtend.frequent_patterns import apriori
    from mlxtend.frequent_patterns import association_rules   
    from mlxtend.preprocessing import TransactionEncoder	
    #pd.options.display.max_columns=100
    # 定义模型，因为mlxtend的数据参数有特定模式，这里必须进行独热编码
    te = TransactionEncoder()	
    transaction_tf=te.fit_transform(transaction)
    dfs = pd.DataFrame(transaction_tf,columns=te.columns_)
    # print(dfs)
    #利用apriori函数进行调用计算
    itemsets = apriori(dfs,min_support=0.02,use_colnames=True)
    #此处为了对比，不用lift进行计算，而用了和对比组相同的置信度进行计算，均为置信度=0.3
    rules = association_rules(itemsets, metric="confidence", min_threshold=0.3)
    print("频繁项集：", itemsets)
    print("关联规则：", rules[ (rules['lift'] >= 1) & (rules['confidence'] >= 0.3) ])
    # print("关联规则：",rules)
    # print(rules['confidence'])

#调用函数，经过对比可得两种计算结果相同，频繁项集103个，关联规则20个，经仔细校验，20条关联规则完全相同
efficient_apriori_func()
mlxtend_appriori_func()







