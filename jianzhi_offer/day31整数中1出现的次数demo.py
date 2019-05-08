# Author: Baozi
#-*- codeing:utf-8 -*-
"""
题目描述
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,
并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""
"""解题思路：
1.最简单的思路就是累加1至n中每个整数1出现的次数。我们可以通过对10求余数判断整数的个位数字是不是1.
如果这个数字大于10，除以10之后再判断个位数字是不是1.
"""
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        if not isinstance(n,int):
            return  None
        ret = 0
        for i in range(1,n+1):
            ret += self.WetherHas1(i)
        return ret

    def WetherHas1(self,number):
        result = 0
        while number:
            if number % 10 == 1:
                result += 1
            number /= 10
        return result