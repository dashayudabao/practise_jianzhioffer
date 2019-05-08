# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
class Solution:
    def rectCover(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        tmp1 = 1
        tmp2 = 2
        for i in range(2,number):
            result = tmp1 + tmp2
            tmp1 = tmp2
            tmp2 = result
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.rectCover(1))
    print(s.rectCover(2))
    print(s.rectCover(3))
    print(s.rectCover(4))