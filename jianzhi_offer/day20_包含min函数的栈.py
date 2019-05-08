# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""
#思路：参考剑指offer，利用一个辅助栈来保存当前栈中的最小值。
class Solution:
    def __init__(self):
        self.s_data = []#数据栈
        self.s_min = []#辅助栈

    def push(self, node):
        self.s_data.append(node)
        if len(self.s_min)== 0 or node < self.s_min[-1]:
            self.s_min.append(node)
        else:
            self.s_min.append(self.s_min[-1])

    def pop(self):
        if len(self.s_data)==0:
            return None
        self.s_data.pop()
        self.s_min.pop()

    def top(self):
        if len(self.s_data)==0:
            return None
        tmp = self.s_data.pop()
        self.s_data.append(tmp)
        return tmp


    def min(self):
        if len(self.s_data)==0:
            return None
        print( self.s_min[-1])


if __name__=='__main__':
    a = Solution()
    a.push(3)
    a.min()
    a.push(2)
    a.push(4)
    a.push(0)
    a.min()
    a.pop()
    a.min()
    a.pop()
    a.min()


