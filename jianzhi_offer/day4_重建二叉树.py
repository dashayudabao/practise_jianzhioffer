# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""
#定义树的结构
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def reConstructBinaryTree(pre,tin):
    if not pre or not tin:
        return None
    if set(pre) != set(tin):
        return None
    i = tin.index(pre[0])
    # 常常犯的错误！！root = pre[0]
    root = TreeNode(pre[0])
    root.left = reConstructBinaryTree(pre[1:i+1],tin[:i])
    root.right = reConstructBinaryTree(pre[i+1:],tin[i+1:])
    return root

# 非递归前序遍历
# 当p非空或stack非空时，输出p.data并将p压入stack，遍历左子树
# 当无左子树时，弹出stack，遍历该节点的右子树
def preOrder1(TreeRootNode):
    if TreeRootNode is None:
        return None
    stack = []
    p = TreeRootNode
    print("前序遍历")
    while p or stack:
        while p:
            print(p.data)
            stack.append(p)
            p = p.left
        p = stack.pop().right

#非递归中序遍历
#判断栈和树是否为空，若不，则判断树是否为空，
# 不为空则进栈，然后遍历左子树，若为空，则出栈，输出数据，然后遍历右子树
#
def InOrder2(TreeRootNode):
    if TreeRootNode is None:
        return None
    stack = []
    p = TreeRootNode
    print("中序遍历")
    while p or stack:
        while p:
            stack.append(p)
            p = p.left
        p = stack.pop()
        print(p.data)
        p = p.right

#非递归后序遍历
#后序遍历的非递归实现是三种遍历方式中最难的一种，
#对于任一结点P，将其入栈，然后沿其左子树一直往下搜索，直到搜索到没有左孩子的结点，
# 此时该结点出现在栈顶，但是此时不能将其出栈并访问， 因此其右孩子还为被访问。
# 所以接下来按照相同的规则对其右子树进行相同的处理，当访问完其右孩子时，该结点又出现在栈顶，
# 此时可以将其出栈并访问。这样就 保证了正确的访问顺序。可以看出，在这个过程中，每个结点都两次出现在栈顶，
# 只有在第二次出现在栈顶时，才能访问它。因此需要多设置一个变量标识该结点是 否是第一次出现在栈顶
#上述过程过于复杂，于是转换思路：后序遍历顺序：左、右、根。反过来就是根、右、左，利用前序遍历的思想
#参考：https://www.cnblogs.com/qiaojushuang/p/7887517.html
def LastOrder3(TreeRootNode):
    if TreeRootNode is None:
        return None
    stack = []
    tmp = []
    p = TreeRootNode
    print("后序遍历")
    while p or stack:
        while p:
            # print(p.data)
            tmp.append(p.data)
            stack.append(p)
            p = p.right
        p = stack.pop().left
    result = tmp[::-1]
    for i in result:
        print(i)


if __name__ == '__main__':
    p = [1,2,4,7,3,5,6,8]
    t = [4,7,2,1,5,3,8,6]
    r = reConstructBinaryTree(p,t)
    # preOrder1(r)
    # InOrder2(r)
    LastOrder3(r)
