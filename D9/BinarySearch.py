def binarySearch1(aList, item):  # 针对顺序列表而言O(logn)
    first = 0
    found = False
    last = len(aList) - 1
    while last >= first and not found:
        mid = (first + last) // 2
        if aList[mid] == item:
            found = True
        else:
            if aList[mid] > item:
                last = mid - 1
            else:
                first = mid + 1
    return found


def binarySearch2(aList, item):#带返回值的递归函数，每层都必须return，不然末层return的值会在中途丢失
#----------------------------结束条件-----------------------------#
    if len(aList) == 0:
        return False
    else:
        mid = len(aList) // 2
        if aList[mid] == item:
            return True
# ---------------------------结束条件-----------------------------#
        else:
# --------------------规模减小 调用自身-----------------------------#
            if aList[mid] > item:
                return binarySearch2(aList[:mid], item)# return
            else:
                return binarySearch2(aList[mid + 1:], item)# return
# --------------------规模减小 调用自身-----------------------------#


testList2 = [1, 23, 54, 65, 74, 80, 87, 135]
print(binarySearch2(testList2, 135))
