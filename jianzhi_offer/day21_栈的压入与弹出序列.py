# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列
对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）
"""
#解题思路1：
# 本道题的关键是如果下一个弹出的数字刚好是栈顶数字，那么直接弹出；
# 否则继续压入数字，直到与下一个弹出的数字相等为止
class Solution:
    def IsPopOrder1(self,pPush, pPop):
        if not isinstance(pPush,list) and not isinstance(pPop,list):
            return False
        if len(pPop)!= len(pPush):
            return False
        stack = []
        j = 0
        for i in pPush:
            stack.append(i)
            while stack and stack[-1] == pPop[j]:
                stack.pop()
                j += 1
        if stack:
            return False
        return True
#解题思路2：使用一个辅助栈, 如果辅助栈栈顶元素不等于出栈元素，则从入栈中找改值，直到入栈为空
#如果最后出栈序列为空，则是入栈的弹出序列值
    def IsPopOrder2(self,pPush, pPop):
        if not pPush or not pPop:
            return False
        if len(pPop)!= len(pPush):
            return False
        stack = []#辅助栈
        while pPop:
            pop_val = pPop[0]
            if stack and stack[-1] == pop_val:#stack[-1]表示栈顶元素
                stack.pop()
                pPop.pop(0)
            else:
                while pPush:
                    if pop_val != pPush[0]:
                        stack.append(pPush.pop(0))
                    else:
                        pPush.pop(0)
                        pPop.pop(0)
                        break
                # 此时判断的是当入栈(pPush)已遍历完但是辅助栈(stack)顶元素并非是出栈(pPop)的栈顶元素
                if not pPush:
                    while stack:
                        if stack.pop() != pPop.pop(0):
                            return False
        return True

if __name__ == '__main__':
    list1 = [1,2,3,4,5]
    list2 = [4,5,3,2,1]
    # list2 = [4,5,1,2,3]
    # list2 = [1,2,3,4,5]
    s = Solution()
    print(s.IsPopOrder1(list1,list2))
    print(s.IsPopOrder2(list1,list2))
