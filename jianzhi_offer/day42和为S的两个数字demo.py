# Author: Baozi
#-*- codeing:utf-8 -*-

"""题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，
输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
"""

"""解题思路：
1.这个题最直接的思路就是先在数组中固定一个数，再依次判断数组中的其余的n-1个数字与它的和是不是等于S.
2.为了寻找更好的算法，我们先在数组中选择两个数字，如果它们的和等于输入的S，我们就找到了要找的两个数字，
如果和小于S，我们希望两个数字的和再大一点。由于数组已经排好序，我们可以考虑选择较小数字后面的数字。
同样的，如果两个数字的和大于输入的S，我们可以选择较大数字前面的数字。
"""

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array or not isinstance(array,list):
            return []
        small,big= 0,len(array)-1
        while small < big:
            cursum = array[small] + array[big]
            if tsum == cursum:
                return [array[small],array[big]]
            elif tsum > cursum:
                small += 1
            else:
                big -= 1
        return []


if __name__ == '__main__':
    s = Solution()
    array = [1,2,4,7,8,11,15]
    print(s.FindNumbersWithSum(array,26))
