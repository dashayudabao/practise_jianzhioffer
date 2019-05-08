# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，
最长路径的长度为树的深度。
"""
"""解题思路：
如果一棵树只有一个结点，它的深度为1。如果根结点只有左子树而没有右子树，那么树的深度应该是
其左子树的深度加1；同样如果根结点只有右子树而没有左子树，那么树的深度就是其右子树的深度加1。
如果既有左子树又有右子树，那么树的深度就是其左右深度较大的值再加1.
"""

class TreeNode:
    def __init__(self, data,left=None,right=None):
        self.val = data
        self.left = left
        self.right = right

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if left>right:
            return left+1
        else:
            return right+1


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.right = node6
    node5.left = node7

    a = Solution()
    print(a.TreeDepth(node1))