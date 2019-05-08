# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
class Solution:
    def jumpFloorII(self, number):
        if number == 1:
            return 1
        result = 1
        for i in range(1,number):
            result *= 2
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloorII(4))
    print(s.jumpFloorII(11))