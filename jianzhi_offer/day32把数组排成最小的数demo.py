# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323
"""
"""解题思路：
1.最直接的做法就是先求出这个数组的所有数字的全排列，然后把每个排列拼接起来，最后求出拼起来的数字的最小值。

2.我们可以找到一个排序规则，根据这个规则排序之后能找到一个最小的数字，
python (python3中重定义比较规则和C++中sort函数不一样；并且python3中list的sort函数取消了cmp这个参数，无法将
在函数中定义的规则直接传入，需要借助functools包。
将老式的比较函数（comparison function）转化为关键字函数（key function）。与接受key function的工具一同使用(如
sorted(), min(), max(), heapq.nlargest(), itertools.groupby())。该函数主要用来将程序转成Python 3 格式的，因
为 Python 3 中不支持比较函数。比较函数是可调用的，接受两个参数，比较这两个参数并根据他们的大小关系返回负值、零
或正值中的某一个。关键字函数也是可调用的，接受一个参数，同时返回一个可以用作排序关键字的值。
　　例如：sorted(iterable, key=cmp_to_key(locale.strcoll))
"""



from functools import cmp_to_key

class Solution2:
    def PrintMinNumber(self, numbers):
        # numbers = map(str, numbers)#这一行与下一行同样的功能
        numbers=[str(s) for s in numbers]
        # numbers.sort(key=cmp_to_key(self.cmp1))
        # return  "".join(numbers)
        return "".join(sorted(numbers,key=cmp_to_key(self.cmp1)))

        # lmb = cmp_to_key(lambda n1, n2:int(str(n1)+str(n2))-int(str(n2)+str(n1)))
        # numbers = sorted(numbers, key=lmb)
        # 上面两行能够实现同样的功能，不过这里我们将比较方式定义成了函数

    def cmp1(self,a, b):
        t1 = a + b
        t2 = b + a
        if t1 < t2:
            return -1
        elif t1 == t2:
            return 0
        elif t1 > t2:
            return 1



if __name__ == '__main__':

    lis = [3, 5, 1, 4, 2]
    s = Solution2()
    b = s.PrintMinNumber(lis)
    print(b)

