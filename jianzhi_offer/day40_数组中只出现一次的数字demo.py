# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。
"""
"""解题思路：
利用异或运算的性质：任何一个数字异或它自己都等于0.也就是说，如果我们从头到尾依次异或数组中的每一个数字，
那么最终的结果刚好是那个只出现一次的数字，因为那些成对出现的偶数次的数字全部在异或中抵消了。
于是我们可以依次异或数组中的每一个数字，那么最终的结果就是两个只出现一次的数字的异或结果。由于这两个数
肯定字不一样，那么异或的结果肯定不为0，也就是说在这个结果数字的二进制中至少就有一位为1。我们在结果数字
中找到第一个为1的位置，记为第n位。现在我们以第n位是不是1为标准把原数组中的数字分成两个子数组，第一个子
数组中的每个数字的第n位都是1，而第二个子数组中的每个数字的第n位都是0.由于我们分配的标准是数字中的某一位
是1还是0，那么出现了两次的数字肯定被分配到同一个数组（因为两个相同的数字的任意一位都是相同的）。我们不
可能把两个相同的数字分配到不同的子数组中去，于是我们已经把原数组分配成了两个子数组，每个子数组都只包含
一个只出现一次的数字，而其他数字出现了两次。
"""
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return None
        tmp = 0
        for i in array:
            tmp ^= i
        indexOr  = self.GetOrindexFirst1(tmp)
        num1 = 0
        num2 = 0
        for i in array:
            if self.IsBit(i,indexOr):
                num1 ^= i
            else:
                num2 ^= i
        return sorted([num1,num2])


    def GetOrindexFirst1(self,num):
        index = 0
        while num & 1 ==0 and index < 10:
            num = num >> 1
            index += 1
        return index

    def IsBit(self,num,index):
        num = num >> index
        return num & 1


if __name__ == '__main__':

    array = [2,4,3,6,3,2,5,5]
    a = Solution()
    print(a.FindNumsAppearOnce(array))