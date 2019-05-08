# Author: Baozi
#-*- codeing:utf-8 -*-
"""
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向
"""
# 解题思路：原先指向左子节点的指针调整为链表中指向前一个节点的指针
# 原先指向右子节点的指针调整为链表中指向后一个节点的指针

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree or not isinstance(pRootOfTree,TreeNode):
            return None
        #为叶节点则直接返回
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        #处理左子树
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left
        # 连接根与左子树最大结点
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left = left
            left.right = pRootOfTree

        #处理右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right
        # 连接根与右子树最小结点
        if right:
            while right.left:
                right = right.left
            pRootOfTree.right = right
            right.left = pRootOfTree

        #下面是为了返回给主程序使用的
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree

if __name__ == '__main__':
    pNode1 = TreeNode(10)
    pNode2 = TreeNode(6)
    pNode3 = TreeNode(14)
    pNode4 = TreeNode(4)
    pNode5 = TreeNode(8)
    pNode6 = TreeNode(12)
    pNode7 = TreeNode(16)

    pNode1.left, pNode1.right = pNode2, pNode3
    pNode2.left, pNode2.right = pNode4, pNode5
    pNode3.left, pNode3.right = pNode6, pNode7

    s = Solution()
    a = s.Convert(pNode1)
    while a:
        print(a.val, end=' ')
        a = a.right


