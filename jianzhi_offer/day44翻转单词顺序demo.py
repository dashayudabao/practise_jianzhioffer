# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，
有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的
顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
"""
"""解题思路：
首先翻转句子中的所有字符，但是此时我们会将句子中的单词也会翻转。于是第二步我们需要
再翻转每个单词中的顺序。
"""


class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return None
        s = list(s)
        start,end,length = 0,0,len(s)
        self.Reverse(s,0,length-1)
        while start<length:
            if s[start] == '':
                start += 1
                end += 1
            elif end == length or s[end] == ' ':
                self.Reverse(s,start,end-1)
                start =end + 1
                end += 1
            else:
                end += 1
        return ''.join(s)




    def Reverse(self,s,start,end):
        if start>end:
            return  None
        while start<end:
            s[start],s[end] = s[end],s[start]
            start += 1
            end -=1

        return s

if __name__ == '__main__':
    s  = 'I am a student!'
    so = Solution()
    print(so.ReverseSentence(s))