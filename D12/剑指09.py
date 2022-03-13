# 用两个栈实现队列
class CQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []



    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack1.append(value)



    def deleteHead(self):
        """
        :rtype: int
        """
        if self.stack2 !=[]:
            res = self.stack2.pop()
        elif self.stack1 == []:
            res = -1
        elif self.stack1 != []:
            while(self.stack1!=[]):
                self.stack2.append(self.stack1.pop())
            res = self.stack2.pop()
        return res



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()