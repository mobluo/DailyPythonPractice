def shellSort(alist):# 插入排序升级版
    sublistcount = len(alist)//2
    while sublistcount>0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        print("After increments of size ",sublistcount,"The list is ",alist)

        sublistcount = sublistcount//2

def gapInsertionSort(alist,start,gap):
    for i in range(start +gap ,len(alist),gap):
        currentvalue = alist[i]
        position = i
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]= alist[position-gap]
            position = position-gap
        alist[position] = currentvalue


def mergeSort1(aList):
    if len(aList)>1:#结束条件
        mid = len(aList)//2
        lefthalf = aList[:mid]
        righthalf = aList[mid:]#规模减小

        mergeSort1(lefthalf)# 调用自身
        mergeSort1(righthalf)
        print(aList)
        i = j = k =0
        while i <len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                aList[k] = lefthalf[i]
                i =i+1
            else:
                aList[k] = righthalf[j]
                j = j+1
            k = k+1
        while i <len(lefthalf):
            aList[k] = lefthalf[i]
            i = i+1
            k = k+1
        while j <len(righthalf):
            aList[k] = righthalf[j]
            j = j+1
            k = k+1

def mergeSort2(aList):
    if len(aList)<=1:
        return aList
    mid = len(aList)//2
    left = mergeSort2(aList[:mid])
    right = mergeSort2(aList[mid:])

    merged = []

    while left and right:
        if left[0]<=right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged

def quickSort(aList):
    quickSortHelper(aList,0,len(aList)-1)

def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and alist[leftmark]<=pivotvalue:
            leftmark = leftmark+1
        while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done =True
        else:
            alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]
    alist[first],alist[rightmark] = alist[rightmark],alist[first]
    return rightmark



