import itertools
minsupport=2
def loadDataSet(file_name):#读取文件
    data_list = []
    fr=open(file_name,encoding='utf-8-sig') 
    lines = fr.readlines()
    for line in lines:
        pas_line = line.strip().split(" ")
        # flt_line = list(map(eval, pas_line)) #把每行转化为字符串列表
        data_list.append(pas_line) #列表添加每行
    return data_list

def CreateC1(data):#创建c1项集并统计支持度
    c1=[] #创建项集
    for Itemset in data:
        for Items in Itemset:
            if not [Items]  in c1:
                c1.append([Items])
    c1.sort()
    return c1
   
def bijiao(a,b):#返回一个值在某个数据集出现次数
    count=0
    for dataset2 in b:
        for dataitem in dataset2:
            if a == dataitem:
                count +=1
    return count
def Statisticalsupport(datac1,dataset):#统计每项个数
    for everyitemset in datac1:#遍历每个项集
        for everyitems in everyitemset:
            c=bijiao(everyitems,dataset)
        everyitemset.append(c)        
    return datac1

def CreateL1(datac1):#筛选出满足最小支持度的创建为L1
    for dataset in datac1:
        if int(dataset[-1]) < int(minsupport):
                datac1.remove(dataset)
    return datac1
def bijiao2(a,dataset):
    count=0
    for everydataset in dataset:
            if set(a).issubset(set(everydataset))==True:
                count +=1
    return count



def CreateC2(c1,dataset,n):#创建c2
    c2=[]#去除sup
    c3=[]#排列组合的新集合
    c4=[]#加上新的sup
    for itemset in c1:
        c2.append(itemset[0])
    c3=set(itertools.combinations(c2,n))#排列组合2
    for everyitemset in c3:#筛选出来
        count = 0
        for everydataset in dataset:
            if set(everyitemset).issubset(set(everydataset))==True:
                count +=1
                if not list(everyitemset) in c4:
                    c4.append(list(everyitemset))
    c4.sort()   
    return c4
def CreateL2(C2,dataset): #创建L2
    for itemset in C2:
        count =0
        c='1'
        for itemset2 in dataset:   
            if set(itemset).issubset(set(itemset2))==True:
                count += 1
        # print(count)
        
        itemset.append(count)
    for itemset3 in C2:
        if itemset3[-1] < minsupport:
            C2.remove(itemset3)
                
    return C2

    





if __name__ == '__main__':
    dataSet = loadDataSet("myself\data.txt")
    a=CreateC1(dataSet)
    b=Statisticalsupport(a,dataSet)
    c=CreateL1(b)
    d=int(len(c))
    for i in range(1,d+1):
        d=CreateC2(c,dataSet,i)
        e=CreateL2(d,dataSet)
        print('频繁',i,'项集为',e)

    # print(dataSet)
  
