def bubblesort(aList):
    for NumTime in range(len(aList) - 1, 0, -1):
        for i in range(NumTime):
            if aList[i] > aList[i + 1]:
                aList[i], aList[i + 1] = aList[i + 1], aList[i]  # a,b=b,a
    return aList


def selctionSort(aList):
    for NumTime in range(len(aList) - 1, 0, -1):
        max_position = 0
        for i in range(NumTime):
            if aList[max_position] < aList[i + 1]:
                max_position = i + 1
        aList[max_position], aList[NumTime] = aList[NumTime], aList[max_position]
    return aList


def insertSort(aList):
    for index in range(1, len(aList)):
        currentValue = aList[index]  # 取出列表中的index项作为currentvalue，并记录位置
        pos = index
        while pos > 0 and aList[pos - 1] > currentValue:# 比较currentvalue与其之前列表左边的值
            aList[pos] = aList[pos - 1]# 若左边大，则把左边的值移至列表右边的空位
            pos = pos - 1# 位置指针指向左边位置
        aList[pos] = currentValue# currentvalue再放入之前左边值的位置（位置指针指向的位置）
    return aList


testList1 = [1, 23, 545, 65, 7, 3, 87, 35]

# print(bubblesort(testList1))
print(insertSort(testList1))
