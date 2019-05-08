# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
"""
# 解题思路：由于路径是由根节点出发到叶节点的，即路径总是以 根结点为起点，因此我们需
# 遍历根结点，则可以使用前序遍历的方式。
class TreeNode:
    def __init__(self, data= None,left= None,right=None):
        self.val = data
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not isinstance(root,TreeNode):
            return self.result
        if not root:
            return self.result
        currentNumber = 0
        path = []

        self.find_path(root,expectNumber,path,currentNumber)
        return self.result

    def find_path(self,root,expectNumber,path,currentNumber):
        currentNumber += root.val
        path.append(root)

        #满足条件
        isLeaf = root.left == None  and root.right == None
        if currentNumber == expectNumber and isLeaf:
            self.result.append([p.val for p in path])
            # for i in path:
            #     print(i.val,end=' ')



        if root.left:
            self.find_path(root.left,expectNumber,path,currentNumber)
        if root.right:
            self.find_path(root.right,expectNumber,path,currentNumber)

        path.pop()
        # return result

if __name__ == '__main__':
    node1 = TreeNode(10)
    node2 = TreeNode(5)
    node3 = TreeNode(12)
    node4 = TreeNode(4)
    node5 = TreeNode(7)

    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    s = Solution()
    r = s.FindPath(node1, 10)
    # for i in r:
    #     print(i)
