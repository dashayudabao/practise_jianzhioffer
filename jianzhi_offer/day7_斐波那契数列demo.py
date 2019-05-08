# Author: Baozi
#-*- codeing:utf-8 -*-
"""
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""
#用递归形式:时间复杂度为(二叉树的节点个数）：O()=(2^h)-1=2^n。空间复杂度为树的高度：h即O(n)
class Solution:
    def __init__(self,count=0):
        self.count = count#用于计数

    def fib1(self,n,arr):
        if(n==0):
            return 0
        if(n<3):
            return 1
        self.count += 1
        if(arr[n] != -1):
            return arr[n]
        arr[n] = self.fib1(n - 1, arr) + self.fib1(n - 2, arr)
        return arr[n]
    #用循环形式:时间复杂度O(n)
    def fib2(self,n):
        tmp2 = 1
        result = 0
        for i in range(n):#n>3
           tmp1 = tmp2
           tmp2 = result
           result = tmp1 + tmp2
        return result

if __name__ == '__main__':
    # print(fib1(5))
    # print(fib1(7))
    arr = []
    for i in range(100):
        arr.append(-1)
    times = 0
    s = Solution()
    print(s.fib1(60,arr))#记忆化搜索！
    print("count",s.count)
    print(s.fib2(0))
    print(s.fib2(1))
    print(s.fib2(2))
    print(s.fib2(40))
    print(s.fib2(60))
