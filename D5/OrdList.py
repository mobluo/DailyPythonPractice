class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnordList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)  # 先把新节点指向表头节点
        self.head = temp  # 再把head标志指向新节点

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()  # 若寻找到item在表头的情况，则将head标志指向current节点的下一个
        else:
            previous.setNext(current.getNext())  # 跳过current节点


class OrdList:
    def __init__(self):
        self.head = None

    def add(self,item):
        current = self.head
        previous =None
        stop =False
        while current !=None and not stop:
            if current.getData()>item:
                stop =True
            else:
                previous =current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head =temp
        else:
            temp.setNext(current)#temp节点指向current节点
            previous.setNext(temp)#previou节点指向temp节点，从而实现在OrdList中插入temp节点

