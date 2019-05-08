# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,
求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
输入描述:
题目保证输入的数组中没有的相同的数字
数据范围：
	对于%50的数据,size<=10^4
	对于%75的数据,size<=10^5
	对于%100的数据,size<=2*10^5
"""
# 示例1
# 输入 1,2,3,4,5,6,7,0
# 输出 7
# import sys
# sys.setrecursionlimit(1000000)    # 用于修改递归最大深度
"""解题思路：
1.最直接的解法就是顺利扫描整个数组，每扫描到一个数字，逐个比较该数字与其后面的数字的大小。
如果后面的数字比它小，则这两个数字构成逆序对。此算法的时间复杂度大致为O(n^2).
2.另一种思路就是基于归并排序。我们首先将数组分解为两个长度为其原始长度一半的子数组，接着在对其子数组
进行拆分（递归实现），直至拆分成两个长度为1的子数组。接下来一边合并相邻的子数组，一边统计逆序对的数目。
以{7,5,4,6}为例，在一开始的一对长度为1的子数组{7}，{5}中7>5，因此构成一个逆序对（7,5）。同样在第二对
子数组中{6}，{4}中也有逆序对（6,4）。由于我们已经统计了这两对子数组内部的逆序对，因此需要把这两对逆序
对排序，以免重复统计。
"""
import sys
sys.setrecursionlimit(1000000)
class Solution:
    def InversePairs(self, data):
        if not data or not isinstance(data,list):
            return 0
        Copy = [i for i in data]

        count = self.InversePairsCore(data,Copy,0,len(data)-1)
        del Copy
        return count % 1000000007

    def InversePairsCore(self,data,Copy,start,end):
        #递归结束的条件！！！
        if start == end:
            Copy[start] == data[start]
            return 0


        mid = int((start+end)/2)

        left = self.InversePairsCore(Copy,data,start,mid)
        right = self.InversePairsCore(Copy,data,mid+1,end)

        # 下面相当于merge
        # i初始化为前半段最后一个数字的下标，j初始化为后半段最后一个数字的下标
        i,j = mid,end
        indexCopy = end
        count = 0


        while i>=start and j>=mid+1:
            if data[i]>data[j]:
                Copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - mid
            else:
                Copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        while i>=start:
            Copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j>=mid+1:
            Copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1

        return left+count+right

if __name__ == '__main__':
    lis = [7, 5, 6, 4]
    a = Solution()
    b = a.InversePairs(lis)
    print(b)
