# 剑指 Offer 63. 股票的最大利润
# 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少
def maxProfit(self, prices: List[int]) -> int:
    # dic ={}
    # i = 0
    # for price in prices:
    #     d[i] = price
    #     i += 1
    # max = 0
    # for i in range(len(prices)-1,-1,-1):
    #     for _ in range(i):
    #         if prices[i] - prices[_] >= max:
    #             max = prices[i] - prices[_]
    # return max
    cost, profit = float("+inf"), 0  # 表示cost=正无穷
    for price in prices:
        cost = min(cost, price)
        profit = max(profit, price - cost)
    return profit


# 剑指 Offer 10- I. 斐波那契数列
# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）
def fib(self, n: int) -> int:
    f = {}
    f[0] = 0
    f[1] = 1
    for i in range(2, 101):
        f[i] = f[i - 1] + f[i - 2]
        if i > n: break
    return f[n] % 1000000007


# 剑指 Offer 10- II. 青蛙跳台阶问题
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
def numWays(self, n: int) -> int:
    # f = {}
    # f[0] = 1
    # f[1] = 1
    # for i in range(2,101):
    #     f[i] = f[i-1]+f[i-2]
    #     if i>=n: break
    # return f[n]%1000000007
    a, b = 1, 1
    if n > 1:
        for _ in range(n - 1):
            a, b = b, a + b
        return b % 1000000007
    else:
        return 1