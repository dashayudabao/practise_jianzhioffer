# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""
class Solution:
    def jumpFloor(self, number):
        if number == 1:
            return 1
        if  number  == 2:
            return 2
        tmp1 = 1
        result = 2
        for i in range(2,number):
            tmp2 = result
            result = tmp1 + tmp2
            tmp1 = tmp2
        return result

if __name__ == '__main__':
    a = Solution()
    print(a.jumpFloor(1))
    print(a.jumpFloor(2))
    print(a.jumpFloor(3))
    print(a.jumpFloor(4))
    print(a.jumpFloor(5))
    print(a.jumpFloor(100))
