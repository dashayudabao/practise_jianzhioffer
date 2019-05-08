# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,
自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一
个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的
挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一
个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪
个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
"""
"""解题思路：本题就是有名的约瑟夫环问题：
1.利用环形链表模拟圆圈的经典解法。
2.分析每次被删除的数字的规律并直接计算出圆圈中最后剩下的数字。

"""
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n<1 or m<1:
            return -1
        head = Node(0)
        p = head
        for i in range(1,n):
            tmp = Node(i)
            p.next = tmp
            p = tmp
        p.next = head

        p = head
        while n>1:
            for i in range(m-1):
                p = p.next
            #弹出该元素
            temp = p.next
            p.data, p.next = temp.data, temp.next
            n -= 1
        return p.data
if __name__ == '__main__':
    a = Solution()
    print(a.LastRemaining_Solution(5, 3))






