# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""
#解题思路：在后序遍历得到的序列中，最后一个数字是树的根结点的值。
# 输入数组的数字可以分为两部分：第一部分是左子树的结点的值，它们都比根结点的值大；
# 第二部分是右子树结点，它们都比根结点的值大。

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence or len(sequence)<=0:
            return
        if not isinstance(sequence,list):
            return
        length = len(sequence)
        root = sequence[length-1]
        count1 = 0
        for i in range(0,length):
            if sequence[i] < root:
                count1 += 1
            else: break
        for j in range(count1,length):
            if sequence[j] < root:
                return  False
        left = True
        if count1 > 0:
            left = self.VerifySquenceOfBST(sequence[0:count1])
        right = True
        if count1>0 and count1< length-1:
            right = self.VerifySquenceOfBST(sequence[count1:length-1])
        return left and right

if __name__ == '__main__':
    s = Solution()
    # list1 = [7,4,6,5]
    # list1 = [5,7,6,9,11,10,8]
    list1 = [1,2,3,4,5]
    print(s.VerifySquenceOfBST(list1))




