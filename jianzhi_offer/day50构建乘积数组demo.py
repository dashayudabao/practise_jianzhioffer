# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素
B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
"""
"""解题思路：
1.最直观的解法就是用连乘n-1个数字构建整个数组B，显然这个方法需要O(n^2)的时间构建整个数组B。
2.找内在规律：我们可以把B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]看成A[0]*A[1]*...*A[i-1]
和A[i+1]*...*A[n-2]A[n-1]两部分的乘积。不妨定义C[i]=A[0]*A[1]*...*A[i-1],C[i]可以自上而下计算
出来，即C[i]=C[i-1]*A[i-1]。类似的，D[i]=A[i+1]*...*A[n-2]A[n-1],D[i]可以自下而上的计算出来，
D[i]=D[i+1]*A[i+1]
"""
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        if not A or not isinstance(A,list):
            return False
        Carray = [1]
        for i in range(1,len(A)):
            Carray.append(Carray[i-1]*A[i-1])
        Darray = [1]*len(A)
        for i in range(len(A)-2,-1,-1):
            Darray[i] = Darray[i+1]*A[i+1]
        result = []
        for i in range(0,len(A)):
            result.append(Carray[i]*Darray[i])
        return result

if __name__ == '__main__':
    s = Solution()
    A = [3,4,5,6,7]
    a = Solution()
    res = a.multiply(A)
    print(res)