# 前提两字符串 均为小写， 长度相等
# 解法1，逐字对照O(n2)
def anagram_judge1(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    for l1 in list1:
        for l2 in list2:
            if l1 == l2:
                list2.remove(l2)
    if len(list2) == 0:
        res = True
    else:
        res = False
    return res

# 解法2，排序比较 O(nlogn) sort()导致
def anagram_judge2(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    list1 = list1.sort()
    list2 = list2.sort()
    i = 0
    n = len(list1)
    # while (i < n):
    #     if list1[i] == list2[i]:
    #         i = i + 1
    #     else:
    #         res = False
    #         break
    while (i < n) and res == True:
        if list1[i] == list2[i]:
            i = i + 1
        else:
            res = False
    return res

# 解法3，计数比较，将每一个字母映射到其ASCII，并计数，ord(),O(n)，空间换时间
def anagram_judge3(s1, s2):
    n = len(s1)
    pos = 0
    i =0
    tem1 = []
    tem2 = []
    # list1 = list(s1)
    # list2 = list(s2)
    # for l1 in list1:
    #     pos = ord(l1)-ord('a')
    #     tem1[pos] = tem1[pos]+1
    #
    # for l2 in list2:
    #     pos = ord(l2)-ord('a')
    #     tem2[pos] = tem2[pos]+1
    for j in range(n):
        pos = ord(s1[j])-ord('a')
        tem1[pos] = tem1[pos] + 1
    for j in range(n):
        pos = ord(s2[j]) - ord('a')
        tem2[pos] = tem2[pos] + 1

    while i<n and res == True:
        if tem1[i] ==tem2[i]:
            i = i+1
        else:
            res = False
    return res


# 解法4，字典


print(anagram_judge1("pytwqhon", "teryphon"))
