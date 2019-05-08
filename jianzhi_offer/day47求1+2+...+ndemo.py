# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""
"""解题思路：
1.利用内置函数sum和range即可快速实现。
2.利用逻辑与的短路特性实现递归终止
"""
# “and”运算符表示“与”，前一项为假则整个表达式为假，因此可以利用这个性质进行递归运算或者
# 达到整洁代码的目的。
class Solution:
    def Sum_Solution(self, n):
        result = n
        temp = n > 0 and self.Sum_Solution(n-1)
        result += temp
        return result