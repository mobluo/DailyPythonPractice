# 包含min函数的栈
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        if self.stack2 == [] or x <= self.stack2[-1]:
            self.stack2.append(x)

    def pop(self):
        """
        :rtype: None
        """
        res = self.stack1.pop()
        if res == self.stack2[-1]:
            self.stack2.pop()

    def top(self):
        """
        :rtype: int
        """
        res = self.stack1[-1]
        return res

    def min(self):
        """
        :rtype: int
        """
        res = self.stack2[-1]
        return res

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()