# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""
class TreeNode:
    def __init__(self,data=None,left = None,right = None):
        self.val = data
        self.left = left
        self.right = right

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not isinstance(pRoot1,TreeNode) or not isinstance(pRoot2,TreeNode):
            return False

        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.JudgeSubTree(pRoot1.left,pRoot2.left) and self.JudgeSubTree(pRoot1.right,pRoot2.right)
            if not result:
                result = self.HasSubtree(pRoot1.left,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right,pRoot2)
        return result

    def JudgeSubTree(self,p1,p2):
        if not p2:
            return True
        if not p1:
            return False
        if p1.val != p2.val:
            return False
        return self.JudgeSubTree(p1.left,p2.left) and self.JudgeSubTree(p1.right,p2.right)


if __name__ == '__main__':
    # 树1
    node1 = TreeNode(8)
    node2 = TreeNode(8)
    node3 = TreeNode(7)
    node4 = TreeNode(9)
    node5 = TreeNode(2)
    node6 = TreeNode(4)
    node7 = TreeNode(7)

    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node5.left, node5.right = node6, node7

    # 树2
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(3)

    node8.left, node8.right = node9, node10
    s = Solution()

    print(s.HasSubtree(node1, node8))