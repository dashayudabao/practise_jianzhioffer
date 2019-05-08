# Author: Baozi
#-*- codeing:utf-8 -*-
# 面试题39 数组中出现次数超过一半的数字
'''
三种方法：
1.将numbers排序，返回中位数
2.利用一个list来存储数字和该数字出现的次数，最后保存的是出现次数过半的数字
3.利用快排的思想，当快排插入的位置不等于mid时，相应的处理numbers的左边或者右边
    因为当出现的次数超过一半时，中间的数字肯定是结果
    但我这里优化了一下快排，返回的是一个范围
    因为书上的快排方法，会反复的排列重复的数字
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not isinstance(numbers, list) or not numbers:
            return 0
        mid = len(numbers) >> 1
        pivot = self.Partition(numbers,0,len(numbers)-1)
        while mid < pivot[0] or mid > pivot[1]:
            if mid < pivot[0]:
                # 处理左边
                pivot = self.Partition(numbers, 0, pivot[0] - 1)
            else:
                # 处理右边
                pivot = self.Partition(numbers, pivot[1] + 1, len(numbers) - 1)
        result = numbers[mid]
        if self.CheckMoreThanHalf(numbers,result):
            return result
        else:
            return 0

    def Partition(self,numbers,low,high):
        pass

    def CheckMoreThanHalf(self,numbers,number):
        times = 0
        for i in numbers:
            if number == i:
                times += 1
        if times > (len(numbers)>>1):
            return True
        else:
            return False

class Solution_1:
    # 利用将数组进行排序，然后返回中间值
    #1.将numbers排序，返回中位数
    def MoreThanHalfNum_Solution(self, numbers):
        if not isinstance(numbers, list) or not numbers:
            return 0
        mid = len(numbers) >> 1
        numbers.sort()
        result = numbers[mid]
        if self.CheckMoreThanHalf(numbers,result):
            return result
        else:
            return 0

    def CheckMoreThanHalf(self,numbers,number):
        times = 0
        for i in numbers:
            if number == i:
                times += 1
        if times > (len(numbers)>>1):
            return True
        else:
            return False

class Solution_2:
    #2.利用一个list来存储数字和该数字出现的次数，最后保存的是出现次数过半的数字
    def MoreThanHalfNum_Solution(self,numbers):
        if not isinstance(numbers, list) or not numbers:
            return 0
        result = [numbers[0],1]
        for i in numbers[1:]:
            if i == result[0]:
                # 如果该数字与记录的数字相同，则次数加一
                result[1] += 1
            elif result[1] == 0:
                result[0] = i
                result[1] = 1
            else:
                result[1] -= 1
        if self.CheckMoreThanHalf(numbers,result[0]):
            return result[0]
        else:
            return 0

    def CheckMoreThanHalf(self,numbers,number):
        times = 0
        for i in numbers:
            if number == i:
                times += 1
        if times > (len(numbers)>>1):
            return True
        else:
            return False

class Solution_3:
    def MoreThanHalfNum_Solution(self,numbers):
        if not isinstance(numbers, list) or not numbers:
            return 0
        Num_Hash = {}
        for i in numbers:
            Num_Hash[i] = Num_Hash.get(i,0) + 1
        Num_Hash_Sort = sorted(Num_Hash.items(), key=lambda x: x[1], reverse=True)
        if Num_Hash_Sort[0][1] > (len(numbers)>>1):
            return Num_Hash_Sort[0][0]
        else:
            return 0


numbers = [1,2,3,2,2,2,5,4,2]
# a = Solution()
# b = a.MoreThanHalfNum_Solution(c)
# print(b)
# a = Solution_2()
# b = a.MoreThanHalfNum_Solution(numbers)
# print(b)
a = Solution_3()
a.MoreThanHalfNum_Solution(numbers)

