# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""
"""解题思路：
1.因为有了二叉树深度的经验之后在解决这个问题，我们很容易就能想到一个思路：在
遍历树的每个结点的时候，我们利用函数直接求出其左右子树深度之后。如果每个结点
的左右子树深度差都不差过1，按照定义它就是一棵平衡树的二叉树。
2.第一种思路的代码很简洁，但是每个结点可能会重复遍历很多遍，我们考虑一个更加
高效的办法，如果我们用后续遍历的方式遍历二叉树的每个一结点，在遍历结点之前我们
就已经遍历了它的左右子树。只要在遍历每个结点的时候记录它的深度，我们就可以一边
遍历一边判断每个结点是不是平衡的。
"""

class TreeNode:
    def __init__(self, data,left=None,right=None):
        self.val = data
        self.left = left
        self.right = right
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        depth = [0]
        return self.IsBalanced_Solution2(pRoot,depth)

    def IsBalanced_Solution2(self,pRoot,depth):
        if not pRoot:
            depth[0] = 0
            return True
        left,right = [0],[0]
        if self.IsBalanced_Solution2(pRoot.left,left) and self.IsBalanced_Solution2(pRoot.right,right):
            differ = left[0] - right[0]
            if abs(differ)<=1:
                depth[0] = max(left[0],right[0]) + 1
                return True
        return False

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
    print(a.IsBalanced_Solution(node1))