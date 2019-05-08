# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""
#解题思路：为了能够按层的顺序打印结点，我们从根结点开始分析，为了打印值为8的结点的两个子结点，
# 我们应该在遍历到8的时候将其子结点保存到一个容器中，然后先取出值为6的结点打印值为6的结点后
#再把其值为5和7富人两个子结点放入容器中。同理将值为10的两个子结点放入容器，注意值为10的结点比
# 5和7线放入容器，因此该数据容器应该是一个队列。
# 二叉树如下：
#     	     8
#     	   /  \
#     	  6   10
#     	 / \  / \
#     	5  7 9  11


class TreeNode:
    def __init__(self, data,left = None,right = None):
        self.val = data
        self.left = left
        self.right = right
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        result = []
        if not isinstance(root,TreeNode) or not root:
            return result
        myqueue = []
        myqueue.append(root)
        while myqueue:
            p = myqueue.pop(0)
            result.append(p.val)
            print(p.val)
            if p.left :
                myqueue.append(p.left)
            if p.right:
                myqueue.append(p.right)
        return result


if __name__ == '__main__':
    #测试用例1
    # node1 = TreeNode(10)
    # node2 = TreeNode(8)
    # node3 = TreeNode(7)
    # node4 = TreeNode(1)
    # node5 = TreeNode(2)
    # node6 = TreeNode(3)
    # node7 = TreeNode(4)
    # node1.left,node1.right = node2,node3
    # node2.left,node2.right = node4,node5
    # node3.left,node3.right = node6,node7

    #测试用例2
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(3)
    node4 = TreeNode(2)
    node5 = TreeNode(1)
    node1.left,node2.left = node2,node3
    node3.left,node4.left = node4,node5
    s = Solution()
    r =s.PrintFromTopToBottom(None)
    for i in r:
        print(i,end=" ")
