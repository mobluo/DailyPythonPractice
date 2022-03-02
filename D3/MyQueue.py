class MyQueue:
    def __init__(self):
        self.items = []

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def size(self):
        return len(self.items)


def hotPotato(namelist, num):
    simqueue = MyQueue()
    for name in namelist:  # 所有人都加入到队列里面
        simqueue.enqueue(name)
    while simqueue.size() > 1:  # 只要队列里面还有人
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())  # 将队首元素dequeue出去，然后再enqueue到队尾
        simqueue.dequeue()
    return simqueue.dequeue()


# print(hotPotato(["a","b","e","f","y","g","k","u","r"],4))

import random


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def busy(self):
        if self.currentTask == None:
            return False
        else:
            return True

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

def simulation(numSeconds,pagePerMinute):
    labPrint = Printer(pagePerMinute)
    printQueue = MyQueue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if(not labPrint.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labPrint.startNext(nexttask)
        labPrint.tick()
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." %(averageWait,printQueue.size()))

simulation(2000,5)