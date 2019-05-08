# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中第一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
那么对应的输出是第一个重复的数字2。
"""
"""解题思路：
1.解决该问题最简单的方法就是先把输入的数组排序。从排序的数组中找出重复的数字是件很容易的事，
只需从头到尾扫描排序后的数组就可以了。
2.利用哈希表。从头到尾的遍历数组的每个数，每扫描到一个数的时候，都可以用0(1)的时间来判断
哈希表里是否包含该数字。如果哈希表还没有该数字，就把它加入到哈希表里。如果哈希表已经存在
该数字，那么就找到了一个重复的数字。该算法的时间复杂度是0(n),但它提高时间效率是以O(n)为
价的。用字典（键值对）。因为Python对字典的key的存储方式为哈希表
3.找到内在规律解决问题。以数组{2,3,1,0,2,5,3}为例来分析。一开始该数组的第0个数字是2，与第2个
数字1不相等，于是把它和下标为2的数字1交换。交换后的数组是{1,3,2,0,2,5,3}。此时第0个数字是1，
与第1个数字2不相等，将其交换，得到数组{3,1,2,0,2,5,3}。以此类推，交换第0个数字3与第三个数字0，
得到数组{0,1,2,3,2,5,3}。此时第0个数字的数值为0，接着扫描下一个数字，下标为1,2,3的数字和数值
相等，因此不需要做任何操作。接下来扫描到下表为4的数字2.由于它的数值与下标不相等，再比较第2个数字
2，相等说明找到了第一个重复的数字。
4.不需要额外的数组保存，利用题目中说“数组里数字的范围在0到n-1 之间”，所以可以利用现有数组设置
标志，当一个数字被访问过后，可以设置对应位上的数 + n，之后再遇到相同的数时，会发现对应位上的数已
经大于等于n了，那么直接返回这个数即可。
"""

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate1(self, numbers, duplication):
        if not isinstance(duplication,list):
            return False
        # write code here
        # 判断边界条件
        if numbers == None or len(numbers) == 0:
            print('数组为空')
            return False
        # 判断数字在0到n-1的范围内
        Len = len(numbers)
        for i in numbers:
            if i < 0 or i > Len - 1:
                print('值%d不在范围内' % i)
                return False

        flag = True
        while flag:
            for index in range(len(numbers)):
                if index == numbers[index]:
                    continue
                tmp = numbers[index]
                if numbers[tmp] == tmp:
                    duplication.append(tmp) #在Pcharm上这样写才通过
                    # duplication[0] = tmp  #牛客网上这样写才通过
                    print(duplication[0])
                    return True
                else:
                    numbers[tmp],numbers[index] = numbers[index],numbers[tmp]
            flag = False

        return False

    def duplicate2(self, numbers, duplication):
        dict = {}
        for num in numbers:
            if num not in dict:
                dict[num] = 0
            else:
                duplication[0] = num
                return True
        return False

    def duplicate3(self, numbers, duplication):
        long = len(numbers)
        for i in range(len(numbers)):
            index = numbers[i]%long if numbers[i] >= long else numbers[i]
            if numbers[index] > long:
                duplication[0] = index
                return True
            numbers[index] += long
        return False




if __name__ == '__main__':
    s = Solution()
    print(s.duplicate1([2,1,3,1,4],[]))
    # print(s.duplicate2([2,1,3,1,4],[]))
    # print(s.duplicate3([2,1,3,1,4],[]))
