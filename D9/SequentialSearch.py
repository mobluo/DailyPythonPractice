def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


def OrdSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            stop = True
        else:
            pos = pos + 1
    return found


testList1 = [1, 23, 545, 65, 7, 3, 87, 35]
testList2 = [1, 23, 54, 65, 74, 80, 87, 135]
print(sequentialSearch(testList2, 23))
