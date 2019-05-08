# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入两个链表，找出它们的第一个公共结点。
"""
"""解题思路：
1.蛮力法：在第一个链表顺序遍历每个结点，每遍历到一个结点时，在第二个链表上遍历每个结点，如果在第二个链表上
有一个结点和第一个链表上的结点一样，说明两个链表在这个结点上重合，于是就找到了它们的公共结点。此方法的时间
复杂度为O(n*m).
2.借助辅助栈：分别把两个链表的结点放入栈中，这样两个链表的尾结点就位于两个栈的栈顶，接下来比较两个栈顶的结
点是否相同。如果相同，则把栈顶弹出接着比较下一个栈顶，直到找到最后一个相同的结点。此方法的时间复杂度为O(n+m),
空间复杂度为O(m+n).
3.结合长度的方法：首先遍历两个链表得到它们的长度，就能知道哪个链表更长以及长的链表比短的链表多几个结点。在第
二次遍历的时候，让较长的链表先走若干步，使其走到与短链表同样长度的位置然后同时在两个链表上同时遍历，找到的第
一个相同的结点就是它们的公共结点。
4.上一种方法的改进：这种方法不需要计算链表的长度，是上一种方法的改进，当两链表一样长的时候，它们的公共节点的
数目是一样，所以此时大家一起前进，会有p1==p2的情况，当两链表不等长的时候，当短的链表走完的时候，它会重新指向
长的链表，然后当长的链表走完的时候，会指向短的链表。此时，两链表到公共节点的距离就相等了。因为当短链表走完时，
两指针之间的差值就相当于上面的nLengthDiffer。
"""
class ListNode:
    def __init__(self, data=None,next= None):
        self.val = data
        self.next = next
class Solution:
    def FindFirstCommonNode3(self, pHead1, pHead2):
        if not isinstance(pHead1,ListNode) and isinstance(pHead2,ListNode):
            return None
        if not pHead1 and not pHead2:
            return None
        len1 = self.getLisnodeLength(pHead1)
        len2 = self.getLisnodeLength(pHead2)
        step = abs(len1 - len2)
        pLong,pShort = pHead1,pHead2
        if len1<len2:
            pLong,pShort = pHead2,pHead1

        for i in range(step):
            pLong = pLong.next

        while pLong and pShort and pLong != pShort:
            pLong = pLong.next
            pShort = pShort.next

        return pLong

    def getLisnodeLength(self,phead):
        if not phead:
            return 0
        p = phead
        l = 0
        while p:
            l += 1
            p = p.next
        return l

    def FindFirstCommonNode4(self,pHead1,pHead2):
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            p1 =p1.next if p1 != None else pHead2
            p2 =p2.next if p2 != None else pHead1
        return p1








if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)

    node1.next = node2
    node2.next = node3
    node3.next = node6
    node6.next = node7
    node4.next = node5
    node5.next = node6

    a2 = Solution()
    b = a2.FindFirstCommonNode4(node1, node4)
    print(b.val)


