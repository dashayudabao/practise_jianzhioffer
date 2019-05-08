# Author: Baozi
#-*- codeing:utf-8 -*-\
"""题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
输入描述:
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
"""
class TreeNode:
    def __init__(self, data=None,left= None,right=None):
        self.val = data
        self.left = left
        self.right = right
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not isinstance(root,TreeNode):
            return None
        if not root: return None
        root.left,root.right = root.right,root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root

    def printTree(self,root):
        if not root:return None
        if not isinstance(root,TreeNode):return None
        print(root.val)
        self.printTree(root.left)
        self.printTree(root.right)


if __name__ == '__main__':
    node1 = TreeNode(10)
    node2 = TreeNode(8)
    node3 = TreeNode(7)
    node4 = TreeNode(1)
    node5 = TreeNode(2)
    node6 = TreeNode(3)
    node7 = TreeNode(4)

    node1.left,node1.right = node2,node3
    node2.left,node2.right = node4,node5
    node3.left,node3.right = node6,node7


    s = Solution()
    s.printTree(node1)
    t = s.Mirror(node1)
    s.printTree(t)
