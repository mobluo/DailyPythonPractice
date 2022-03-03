class Deque:
    def __init__(self):
        self.items = []

    def addRear(self, item):  # 左尾 右首
        self.items.insert(0, item)

    def addFront(self, item):
        self.items.append(item)

    def removeRear(self):
        return self.items.pop(0)

    def removeFront(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def palchecker(s):
    res = True
    palList = Deque()
    for _ in s:
        palList.addRear(_)
    n = len(s) // 2
    i = 0
    # if len(s) % 2 == 0:
    while i < n and res:
        if palList.removeRear() == palList.removeFront():
            i += 1
        else:
            res = False

    # else:
    #     while i < n and res:
    #         if palList.removeRear() == palList.removeFront():
    #             i += 1
    #         else:
    #             res = False
    return res

def palchecker1(s):
    chardeque = Deque()
    for ch in s:
        chardeque.addRear(ch)
    stillEqual = True
    while chardeque.size()>1 and stillEqual:#chardeque.size()>1,避免奇偶情况考虑，，len(s)//2，对2取余也可以
        first =chardeque.removeFront()
        last = chardeque.removeRear()
        if first !=last:
            stillEqual = False
    return stillEqual



print(palchecker("asdsa"))
