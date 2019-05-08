# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示
"""
class Solution:
    #此方法只适用于正整数的情况
    #思路：先判断整数的最右边一位是不是1，接着将整数右移一位，
    # 此时从右边数的第二位被移到最右边了，再判断是不是1。
    # 这样，每移动一位直到整个整数变成0为止。
    def NumberOf1_1(self, n):
        flag = 1
        count = 0
        while n:
            if n&flag:
                count += 1
            n = n >> 1
                # print("a"*10)
            # print(n)
        return count
    #高效简洁的方法
    #思路：把一个整数减去1，再和原整数做与运算，会把该整数的最右边一个1变成0.
    #那么一个整数的二进制表示中有多少个1，就可以进行多少次这种操作。

    def NumberOf1_2(self,n):
        count =  0
        while n:
            count += 1
            n = n & (n-1)
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1_1(7))
    print(s.NumberOf1_1(8))
    print(s.NumberOf1_1(9))
    print(s.NumberOf1_2(7))
    print(s.NumberOf1_2(8))
    print(s.NumberOf1_2(9))