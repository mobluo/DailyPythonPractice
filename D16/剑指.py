# 剑指 Offer 11. 旋转数组的最小数字
def minArray(numbers):
    n = len(numbers)
    i = 1
    min = numbers[0]
    for i in range(n):
        if min > numbers[i]:
            min = numbers[i]
        else:
            i = i + 1
    return min

list= [2,2,2,0,1]
print(minArray(list))

# 剑指 Offer 04. 二维数组中的查找
# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
    res = False
    i, j = len(matrix) - 1, 0
    while i >= 0 and j < len(matrix[0]):
        if matrix[i][j] > target:
            i -= 1
        elif matrix[i][j] < target:
            j += 1
        else:
            return True

    return res

# 面试题50. 第一个只出现一次的字符
def firstUniqChar(self, s: str) -> str:
    res = ' '
    dic = {}
    i = 0
    n = len(s)
    for _ in s:
        if _ not in dic:
            dic[_] = 1
        else:
            dic[_] = dic[_] + 1
    for d in dic:
        if dic[d] == 1:
            res = d
            break
    return res