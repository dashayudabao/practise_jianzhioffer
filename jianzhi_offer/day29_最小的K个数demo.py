# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""
"""解题思路:
解法1：最简单的思路就是把输入的n个整数排序，排序之后位于最前面的k个数就是最小的k个数。
解法2：利用Partition函数来解决这个问题。如果基于数组的第k个数字来调整，使得比第k个数字小的所有数字都
位于数组的左边，比第k个数字大的都为数组的右边，这样调整之后，位于数组中左边的k个数字就是最小的k个数字，
但是此时左边的k个数字不一定是有序的。O(n)的算法，只有当我们可以修改输入的数组时使用。
解法3：创建一个大小为k的数据容器来存储最小的k个数字，接下来每次从输入的n个整数中读入一个数。如果容器中
已有的数字少于k个数，则直接把这次读入的整数放入容器中，如果容器中已有k个数字，即容器已满，此时我们不能再
插入新的数字而只能替换已有的数字。而是找出这已有的k个数中的最大值，然后拿这次待插入的整数和最大值进行比较。
如果待插入的值比当前已有的最大值还要大，则替换掉当前的最大值。
"""
class Solution:
    def GetLeastNumbers_Solution1(self, tinput, k):
        # write code here
        if not tinput or len(tinput)<k or k<=0:
            return  []
        pivot = self.Partition(tinput,0,len(tinput)-1)
        while pivot != k-1:
            if pivot > k :
                pivot = self.Partition(tinput,0,pivot-1)
            else:
                pivot = self.Partition(tinput,pivot+1,len(tinput)-1)

        return tinput[:pivot+1]

    def Partition(self,tinput,begin,end):
        key = tinput[begin]
        while begin < end:
            while begin < end and tinput[end] >= key:
                end -= 1
            tinput[begin],tinput[end] = tinput[end],tinput[begin]
            while begin < end and key <= tinput[end]:
                begin += 1
            tinput[begin], tinput[end] = tinput[end], tinput[begin]

        return begin


    def GetLeastNumbers_Solution2(self,tinput, k):
        # vec = tinput[:k]
        vec = [x for x in tinput[:k]]
        max_index = self.find_max(vec)
        for x in tinput[k:]:
            if x < vec[max_index]:
                vec[max_index] = x
                max_index = self.find_max(vec)

        return vec

    def find_max(self,array):
        return array.index(max(array))

if __name__ == '__main__':
    tinput = [4, 5, 1, 6, 2, 7, 8, 3]
    s = Solution()
    a = s.GetLeastNumbers_Solution1(tinput, 4)
    b = s.GetLeastNumbers_Solution2(tinput, 4)
    print(a)
    print(sorted(a))
    print(b)
    print(sorted(b))
