# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述:输入一个字符串,包括数字字母符号,可以为空
输出描述:如果是合法的数值表达则返回该数字，否则返回0
"""
"""解题思路：
Python中str无相减，所以要利用ord()函数，将其转换成ascii码
"""
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s or not isinstance(s,str):
            return 0
        if s[0]=='+':
            return self.StrToInt2(s[1:])
        elif s[0]=='-':
            return -1*self.StrToInt2(s[1:])
        else:
            return self.StrToInt2(s)

    def StrToInt2(self,s):
        if not s:
            return 0
        num = 0
        for i in s:
            if ord(i)<ord('0') or ord(i) > ord('9'):
                return 0
            else:
                num = 10*num +(ord(i) - ord('0'))#转换过程！
        return num

if __name__ == '__main__':
    s = Solution()
    print(s.StrToInt('-1314'))