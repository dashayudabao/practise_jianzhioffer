# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,
他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:
18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
"""
"""解题思路：
我们考虑用两个数small和big分别表示序列的最小值和最大值。首先初始化small为1，big为2.
如果从small到big的序列的和大于s，我们可以从序列中去掉较小的值，也就是增大small的值。
如果从small到big的值小于s，我们可以增大big，让这个序列包含更多的数字。因为这个序列
至少要有两个数字，我们一直增加small到(1+s)/2位置即可。
"""
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 0 or tsum < 3:
            return []
        res = []
        small,big = 1,2
        mid = (1+tsum) >> 1 # 这步是为了循环停止，让small都大于中间的数了，怎么相加都会大于tsum
        cursum = small + big
        while small < mid:
            if cursum == tsum:
                res.append(list(range(small,big+1)))
            while cursum > tsum and small < mid:# 这里需要用循环，而不是if
                cursum -= small
                small += 1
                if cursum == tsum:
                    res.append(list(range(small,big+1)))
            big += 1
            cursum += big
        return res

if __name__ == '__main__':
    s = Solution()
    tmp = s.FindContinuousSequence(1000)
    print(tmp)