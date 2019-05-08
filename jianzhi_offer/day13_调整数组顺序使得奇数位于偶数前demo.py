# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""
#思路：从头开始遍历找到第一个偶数后，然后将其后面的遇到的奇数依次插入到该偶数的前面。
class Solution:
    def reOrderArray(self, array):
        peven = 0
        length = len(array)
        if length<=1:
            return array
        while ((array[peven]&1 == 1) and peven < length):
            peven += 1
        print("start peven",array[peven])
        podd = peven
        while podd < length:
            while (podd < length and (array[podd]&1 != 1)):
                podd += 1
            if peven<podd and podd < length:
                tmp = array[podd]
                for i in range(podd,peven-1,-1):
                    array[i] = array[i-1]
                array[peven] = tmp
                peven += 1
        return array



if __name__ == '__main__':
    s = Solution()
    l = [0,2,3,4,5,6,7,8,9,10]
    print("原始数组为：",l)
    print(s.reOrderArray(l))
    print("调整数组为：",l)