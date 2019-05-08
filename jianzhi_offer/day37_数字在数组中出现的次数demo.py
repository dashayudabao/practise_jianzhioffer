# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
统计一个数字在排序数组中出现的次数。例如输入排序数组{1,2,3,3,3,3,4,5}和数字3,
由于3在这个数组中出现了4次，因此输出4.
"""
"""解题思路：
1.直观的解法：由于是排序数组，我们自然而然的会想到用二分查找算法。在上面的例子中，我们先用
二分查找找到一个3，但3可能出现多次，因此我们找到的3的左右两边可能都有3，于是我们在3的左右两
边顺序扫描，分别找到第一个3和最后一个3.因为要查找的数字在长度为n的数组中有可能出现0(n)次，
所以顺序扫描时间复杂度是0(n).
2.更好地利用二分查找：我们利用二分其实是可以直接找到第一个k值的，当我们找到k值后，我们可以在判断一下
这个数字是不是第一个k。即如果位于该数字前面的一个数字不是k，则此时二分查找的中间数字就是第一个k；如果
中间数字的前一个数字也是k则说明第一个k值在前半段，下一轮仍在数组的前半段查找就好。
"""

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if not data:
            return 0
        length = len(data)
        first = self.GetFirstK(data,k,length)
        last = self.GetLastK(data,k,length)
        result = 0
        if first>-1 and last>-1:
            result = last - first + 1
        return result

    def GetFirstK(self,data,k,length):
        start,end= 0,length-1
        while end >= start:#这里一定要加上等于号，否则找不到
            mid = int((start + end) / 2)
            if data[mid] == k:
                if (mid > 0 and data[mid-1] != k) or mid == 0:
                    return mid
                else:
                    end = mid - 1
            elif data[mid]>k:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def GetLastK(self,data,k,length):
        start, end = 0, length - 1
        while end >= start:#这里一定要加上等于号，否则找不到
            mid = int((start + end)/2)
            if data[mid] == k:
                if (mid < length - 1 and data[mid+1] != k) or mid == length - 1:#注意下标的范围
                    return mid
                else:
                    start = mid + 1
            elif data[mid]>k:
                end = mid - 1
            else:
                start = mid + 1
        return -1

if __name__ == '__main__':
    s = Solution()
    lis = [1,3,3,3,3,4,5]
    print(s.GetNumberOfK(lis,2))
    print(s.GetFirstK(lis,2,7))
    print(s.GetLastK(lis,2,7))