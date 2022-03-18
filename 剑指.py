# 面试题32 - I. 从上到下打印二叉树
# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
def levelOrder(self, root: TreeNode) -> List[int]:
    if not root: return []
    queue = [root]
    res = []
    while queue:
        for _ in range(len(queue)):
            Node = queue.pop(0)
            res.append(Node.val)
            if Node.left: queue.append(Node.left)
            if Node.right: queue.append(Node.right)
    return res

# 剑指 Offer 32 - II. 从上到下打印二叉树 II
# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root: return []
    queue = [root]

    res = []
    while queue:
        tmp = []
        for _ in range(len(queue)):
            Node = queue.pop(0)
            tmp.append(Node.val)
            if Node.left:
                queue.append(Node.left)
            if Node.right:
                queue.append(Node.right)
        res.append(tmp)
    return res


# 剑指 Offer 32 - III. 从上到下打印二叉树 III
# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root: return []
    res = []
    queue = [root]
    while (queue):
        tmp = []
        for _ in range(len(queue)):
            Node = queue.pop(0)
            tmp.append(Node.val)
            if Node.left: queue.append(Node.left)
            if Node.right: queue.append(Node.right)
        res.append(tmp)
    for i in range(len(res)):
        if i % 2 != 0:
            res[i] = res[i][::-1]
        else:
            i += 1
    return res