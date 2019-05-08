# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
如果当前字符流没有存在出现一次的字符，返回#字符。
"""
"""思路
和前面的那道字符串中只出现一次的字符相似而不相同，前面那道是固定长度字符串，而本题是字符流，
也就是会增长的，每次字符串多一个字符，就要重新判断是哪个只出现一次的字符因为牛客网里剑指offer
的python只有2.7，没有3.0以上的版本，而python2.7的字典遍历通常不是有序的（python3通常有序），
所以只能再借助一个列表来存储全部字符串，遍历字符串从而寻找
"""
class Solution:
    # 返回对应char
    def __init__(self):
        self.charlist = []
        self.chardict = {}

    def FirstAppearingOnce(self):
        # write code here
        for key in self.charlist:
            if self.chardict[key] == 1:
                return key

        return '#'

    def Insert(self, char):
        # write code here
        self.chardict[char] = 1 if char not in self.chardict else self.chardict[char]+1
        self.charlist.append(char)