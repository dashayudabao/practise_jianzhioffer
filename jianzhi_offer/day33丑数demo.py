# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它
包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""
'''解题思路：
1.逐个判断每个整数是不是丑数的解法，直观但不够高效：所谓一个数m是另一个数n的因子，是指n能够被m整除，
也就是n%m==0.根据丑数的定义，丑数只能被2,3和5整除。也就是说如果一个数能够被2整除，我们把它连续除以2，
如果能够被3整除，就连续除以3，如果能够被5整除，就连续除以5.如果最后得到的结果是1，那么这个数就是丑数。
2.创建数组保存已经找到的丑数，用空间换时间的解法：第一种方式之所以低效很大程度上是因为不管一个数是不
丑数，我们都要对它做计算。根据丑数的定义，丑数应该是另一个丑数乘以2,3或5的结果。因此我们可以创建一个
数组，里面是排好序的丑数，每一个丑数都是前面的丑数乘以2,3,或5得到的。
'''
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        ret = [1]
        count = 1
        multiple2,multiple3,multiple5= 0,0,0
        while count<index:
            minval = min(ret[multiple2]*2,ret[multiple3]*3,ret[multiple5]*5)
            ret.append(minval)
            while ret[multiple2] * 2 <= ret[-1]:    multiple2 += 1
            while ret[multiple3] * 3 <= ret[-1]:    multiple3 += 1
            while ret[multiple5] * 5 <= ret[-1]:    multiple5 += 1
            count += 1
        return ret[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.GetUglyNumber_Solution(100))

