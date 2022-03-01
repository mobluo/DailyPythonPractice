# 前提两字符串 均为小写， 长度相等
class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)


def parChecker(symbolString):
    s = Stack()
    res = True
    i = 0
    while i < len(symbolString) and res:
        if symbolString[i] == "(":
            s.push(symbolString[i])
        else:
            if s.isEmpty():
                res = False
            else:
                s.pop()
        i = i + 1
    return res


def bracketChecker(symbolString):
    s = Stack()
    i = 0
    res = True
    while i < len(symbolString) and res:
        if symbolString[i] in '({[':
            s.push(symbolString[i])
        else:
            if s.isEmpty():
                res = False
            else:
                if match(s.peek(),symbolString[i]):
                    s.pop()
                else:
                    res = False
        i = i + 1

    return res


# def find(t):
#     pos = 0
#     if t in "({[":
#         for i in "({[":
#             pos = pos + 1
#             if t == i:
#                 break
#     else:
#         for i in ")}]":
#             pos = pos + 1
#             if t == i:
#                 break
#     return pos
#
#
# def match(a,b):
#     if find(a) == find(b):
#         res = True
#     else:
#         res =False
#     return res
def match(open,close):
    opens="({["
    closes=")}]"
    if opens.index(open) == closes.index(close):
        res = True
    else:
        res = False
    return res



print(bracketChecker("(((){}{}[]{{{}}}[]))()"))
