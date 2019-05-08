# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""
'''解题思路：
如果需要判断多个字符是不是在某个字符串里出现过或者统计多个字符在字符串中出现的次数，我们可以考虑
给予数组创建一个简单的哈希表，这样可以用很小的空间消耗换来时间效率的提升。
书上是利用ascii码来建一个数组，而我们可以直接调用python中的dict。
'''
# 在python3.x版本中，dict是的顺序是根据插入时候的顺序的，不会改变
# for i in Hash_Map:
#     if Hash_Map[i] == 1:
#         return i
# 而如果在python2.x版本中，dict的顺序会改变

class Solution:
    def FirstNotRepeatingChar(self, s):
        if not isinstance(s,str):   return -1
        if not s:   return -1
        dict={}
        for i in s:
            dict[i] = dict.get(i,0) + 1
        count = -1
        for i in s:
            count += 1
            if dict[i] == 1:
                return count
        return -1


a = Solution()
print(a.FirstNotRepeatingChar('google'))
