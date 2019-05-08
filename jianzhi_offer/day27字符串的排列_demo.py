# Author: Baozi
#-*- codeing:utf-8 -*-
""" 题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
    输入描述:输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""

def Permutation(lis):
    if not isinstance(lis, list):
        return
    Permutation_(lis, 0)

# 当我们对序列进行交换之后，就将交换后的序列除去第一个元素放入到下一次递归中去了，递归完成了再进行下一次循环。
# 这是某一次循环程序所做的工作，这里有一个问题，那就是在进入到下一次循环时，序列是被改变了。可是，如果我们要
# 假定第一位的所有可能性的话，那么，就必须是在建立在这些序列的初始状态一致的情况下,所以每次交换后，要还原，确
# 保初始状态一致。

def Permutation_(lis, n):
    if n == len(lis):
        print(' '.join(lis))
        return
    for i in range(n, len(lis)):
        # if check(lis, n, i):
        lis[i], lis[n] = lis[n], lis[i]  # 交换两个位置
        Permutation_(lis, n + 1)  # 注意，这里是n+1
        lis[i], lis[n] = lis[n], lis[i]  # 交换回来


def check(lis, n, i):
    # n,i是指这两个元素需要交换
    # 当lis[n]==lis[i]说明两个元素相同，不需要交换，不然会有重复
    if i > n:  # 不用等号是允许自身与自身交换
        # 当不是与自身交换的时候，判断是否会有重复
        for j in range(n, i):
            if lis[j] == lis[i]:
                return False
    return True
lis = list('ab')
Permutation(lis)

# 组合问题：如果输入n个字符，则这n个字符能构成长度为1的组合，长度为2的组合，直到长度为n的组合。
# 因此在求n个字符的长度为m的组合时，我们可以将这n个字符分为两部分：第一部分和其余的所有字符。如
# 果组合里包含第一个字符，则下一步在剩余的字符里面选取m-1个字符，如果不包含第一个字符，则下一步
# 在剩余的n-1个字符里选取m个字符。
# 即最终我们把求n个字符组成的长度为m的组合问题分解为两个字问题：
# 分别求n-1个字符串中长度为m-1的组合，以及求n-1个字符串的长度为m的组合。



# 另外一种递归思路：借助一个辅助列表vec：
# 定义一个Combination_函数：该函数的作用是从长度为n字符串列表lis中，依次循环取出1至m的组合：
# 当vec的长度与所需取出的次数相等时打印出该组合。
def Combination(lis):
    if not isinstance(lis, list):
        return
    vec = []
    for i in range(1, len(lis) + 1):
        Combination_(lis, vec, i)


def Combination_(lis, vec, m):
    if m == len(vec):
        print(' '.join(vec))
        return
    if lis:
        vec.append(lis[0])                  #添加第一个字符进入辅助列表
        Combination_(lis[1:], vec, m)      #递归剩下的m-1个字符，且第一个字符进入辅助列表的情形
        vec.pop()
        Combination_(lis[1:], vec, m)       #递归剩下的m-1个字符，且第一个字符已删除的情形

# lis = list('abc')
# Combination(lis)


# n个皇后问题
def queens(n):
    lis = [x for x in range(n)]
    Permutation_n(lis,0)

def Permutation_n(lis,n):
    if n >= len(lis):
        if SatisfyQueenRequirements(lis):
            print(' '.join(map(str,lis)))
        return
    for i in range(n,len(lis)):
        lis[i],lis[n] = lis[n],lis[i]
        Permutation_n(lis,n+1)
        lis[i],lis[n] = lis[n],lis[i]

def SatisfyQueenRequirements(lis):
    Flag = True
    for i in range(0,len(lis)-1):
        for j in range(i+1,len(lis)):
            if abs(i - j) == abs(lis[i] - lis[j]):
                Flag = False
                break
        if not Flag:
            break
    return Flag


# queens(8)