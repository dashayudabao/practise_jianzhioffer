# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环
左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
"""

"""解题思路：
1.以'abcdefg'为例，我们可以把它分为两部分。第一部分将前n个字符翻转，接着翻转从n+1到末尾的，
最后翻转一下整个字符串就可以了。
2.python还可以利用切片操作，直接对字符串进行切片，同样也是对第n个字符那切片，然后将前后两部分
字符调换一下位置就好了。
"""
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return None
        ss = list(s)
        self.ReverseLeft(ss,0,n-1)
        self.ReverseLeft(ss,n,len(s)-1)
        self.ReverseLeft(ss,0,len(s)-1)
        return ''.join(ss)

    def ReverseLeft(self,s,start,end):
        if start>end:
            return  None
        while start<end:
            s[start],s[end] = s[end],s[start]
            start += 1
            end -=1

        return s

if __name__ == '__main__':
    s1 = 'abcdef'
    d = Solution()
    print(d.LeftRotateString(s1,2))
