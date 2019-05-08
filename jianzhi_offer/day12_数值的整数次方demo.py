# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方
"""
#思路：需要考虑次方是正数、负数和0，基数是0
# 浮点数相等不能直接用==


#############常规解法：考虑全面后，循环得到结果
class Solution:
    def Power1(self, base, exponent):
        if not self.equal(base,0.0) and exponent<0: return None# raise ZeroDivisionError
        if not self.equal(base,0.0) or exponent == 0: return 0.0
        if exponent < 0: return 1/self.Power1(base,-exponent)
        result = 1.
        for i in range(exponent):
            result = result * base
        return result

###############优化解法：利用递归快速求解
    def Power2(self,base,exponent):
        if not self.equal(base,0.0) and exponent<0: return None# raise ZeroDivisionError
        if not self.equal(base,0.0) or exponent == 0: return 0.0
        if exponent < 0: return 1/self.Power1(base,-exponent)
        result = self.Power2(base,exponent >> 1)
        result *= result
        if exponent & 1:
            result *= base
        return result

    def equal(self,num1,num2):
        if ((num1 - num2)<0.00000001 and (num2 - num1)<0.00000001):
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    print("Power1：")
    print(s.Power1(2.,3))
    print(s.Power1(0.0, -2))
    print(s.Power1(0.,3))
    print(s.Power1(1., 0))
    print(s.Power1(-2., -2))
    print(s.Power1(-2., 1))
    print("Power2：")
    print(s.Power2(2.,3))
    print(s.Power2(0.0,-2))
    print(s.Power2(0,3))
    print(s.Power2(1.,0))
    print(s.Power2(-2,-2))
    print(s.Power1(-2., 1))
