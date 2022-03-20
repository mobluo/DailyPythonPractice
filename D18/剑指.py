# 剑指 Offer 26. 树的子结构
# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。
def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
    def recur(A, B):
        if not B: return True
        if not A or A.val != B.val: return False
        return recur(A.left, B.left) and recur(A.right, B.right)

    return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) \
                              or self.isSubStructure(A.right, B))


# 剑指 Offer 28. 对称的二叉树
# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的
def isSymmetric(self, root: TreeNode) -> bool:
    def recur(L, R):
        if not L and not R: return True
        if not L or not R or L.val != R.val: return False
        return recur(L.left, R.right) and recur(L.right, R.left)

    return recur(root.left, root.right) if root else True


# 剑指 Offer 27. 二叉树的镜像
# 请完成一个函数，输入一个二叉树，该函数输出它的镜像
def mirrorTree(self, root: TreeNode) -> TreeNode:
    if not root: return
    root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
    return root