# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针
"""

"""解题思路：
    	    a
    	   /  \
    	  b    c
    	 / \  / \
    	d  e f   g
      	  / \
      	 h   i
上图中这棵二叉树的中序遍历(左根右)是d,b,h,e,i,a,f,c,g,我们以此为例进行分析。
1)如果一个结点有右子树，那么它的下一个结点就是它的右子树中的最左子结点。也就是说从
右结点出发一直沿着指向左指针的结点就能找到它的下一个结点。
2)如果一个结点没有右子树，且它是它父结点的左子树，那么它的下一个结点就是它的父结点。
3）如果一个结点既没有右子树，并且它还是它父结点的右子结点，这种情况相对复杂，我们可以
沿着指向父结点的指针一直向上遍历，直到找到一个是它父结点的左子结点的结点。如果这样的结
点存在，那么这个节点的父结点就是我们要找的下一个结点。
"""
# -*- coding:utf-8 -*-
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent




# def inOrder1(BinaryTreeNode):
    # if BinaryTreeNode == None:
    #     return
    # stack = []
    # p = BinaryTreeNode
    # while p != None or stack:
    #     while p != None:
    #         stack.append(p)
    #         p = p.left
    #     if stack:
    #         s = stack.pop()
    #         print(s.data, end=' ')
    #         p = s.right
    # print()

# def GetNext(BinaryTreeNode):
#     if BinaryTreeNode == None:
#         return
#     cur = BinaryTreeNode
#     if BinaryTreeNode.right:
#         cur = BinaryTreeNode.right
#         while cur.left:
#             cur = cur.left
#         return cur
#     elif cur == cur.parent.left:  # 若节点是父节点的左子树
#         return BinaryTreeNode.parent
#     else:  # 若节点是父节点的右子树
#         while cur.parent.parent and cur.parent == cur.parent.parent.right:
#             cur = cur.parent
#         if not cur.parent.parent:
#             return
#         return cur.parent.parent


if __name__ == '__main__':
    n10 = BinaryTreeNode('i')
    n9 = BinaryTreeNode('h')
    n6 = BinaryTreeNode('g')
    n5 = BinaryTreeNode('f')
    n4 = BinaryTreeNode('e', left=n9, right=n10)
    n3 = BinaryTreeNode('d')
    n2 = BinaryTreeNode('c', left=n5, right=n6)
    n1 = BinaryTreeNode('b', left=n3, right=n4)
    root = BinaryTreeNode('a', left=n1, right=n2)
    n1.parent = root
    n2.parent = root
    n3.parent = n1
    n4.parent = n1
    n5.parent = n2
    n6.parent = n2
    n9.parent = n4
    n10.parent = n4
    inOrder1(root)
    # x = GetNext(n6)
    x = GetNext(n10)
    # x = GetNext(n4)
    print(x.data)