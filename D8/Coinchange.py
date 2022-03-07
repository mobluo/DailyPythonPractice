import time
# 1.贪心策略,可能错过最优解
def changeSolution1(coinValueList, change):
    coinNum = 0
    while change != 0:
        for coin in coinValueList[::-1]:  # 默认给定硬币从小到大排序
            if change >= coin:
                change = change - coin
                coinNum = coinNum + 1
                break  # 跳到for以外
            else:
                continue  # 继续for循环
    return coinNum

# 2.递归算法，耗时
def changeSolution2(coinValueList, change):
    minCoins = change
    if change in coinValueList:#最小规模，直接返回
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:#取列表中小于change的元素作为新列表c
            coinNum = 1 + changeSolution2(coinValueList,change-i)#减小规模，调用自身
            if coinNum < minCoins:
                minCoins = coinNum
    return minCoins

# 3.递归算法 + 记忆表
def changeSolution3(coinValueList, change,knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1 # 列表记录最优解
        return 1
    elif knownResults[change] > 0:#若表中已经有最优结果，则直接用
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            coinNum = 1 + changeSolution3(coinValueList,change-i,knownResults)
            if coinNum < minCoins:
                minCoins = coinNum
                knownResults[change] = minCoins # 记录最优解
    return minCoins

# 4.动态规划
def changeSolution4(coinValueList, change,minCoins):
    for cents in range(1,change + 1):#建表，横轴change长度，纵轴coinValueList中大于change的部分
        coinCount = cents
        for j in [c for  c in coinValueList if c <=change]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        minCoins[cents] = coinCount
    return  minCoins[change]

t1 = time.process_time()
print(changeSolution3([1, 5, 10, 25], 63,[0]*64))#64长度的列表

t2 = time.process_time()
print('time is {}s'.format(t2 - t1))