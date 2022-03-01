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
    list1.sort()                            #重要
    list2.sort()
    i = 0
    n = len(s1)
    res = True
    # while (i < n):
    #     if list1[i] == list2[i]:
    #         i = i + 1
    #     else:
    #         res = False
    #         break
    while (i < n) and res:
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
    tem1 = [0]*26                                       #重要
    tem2 = [0]*26
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

    res = True
    while i<n and res:
        if tem1[i] ==tem2[i]:
            i = i+1
        else:
            res = False
    return res
# 解法4，字典，类似解法3
def anagram_judge4(s1, s2):
    n = len(s1)
    i =0
    list1 =list(s1)
    list2 = list(s2)
    d1 = dict()
    d2 = dict()
    for l1 in list1:
        if l1  not in d1:
            d1[l1] = 1
        else:
            d1[l1] = d1[l1] +1
    for l2 in list2:
        if l2  not in d2:
            d2[l2] = 1
        else:
            d2[l2] = d2[l2] +1

    res = True
    # for l1 in d1:
    #     if d1[l1] == d2[l1]:
    #         continue
    #     else:
    #         res = False
    #         break
    if d1 !=d2:
        res =False

    return  res




# anagram_judge4("pyaatwqhon", "teryphoddn")
print(anagram_judge4("pyweteehon", "typhoeeewn"))
