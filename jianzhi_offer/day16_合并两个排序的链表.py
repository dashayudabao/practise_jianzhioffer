# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""
# 思路：首先考虑两个链表的头结点的大小后，将较小值作为我们新链表的头节点
# 然后依次合并两个链表剩余节点。需要注意代码的鲁棒性：空链表，空节点，其中一个
# 为空的情况等等。

class ListNode:
    def __init__(self, data,next = None):
        self.data = data
        self.next = next
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not isinstance(pHead1,ListNode) and not isinstance(pHead2,ListNode):
            return None
        if not pHead1 and not pHead2: return None
        if not pHead1: return pHead2
        if not pHead2: return pHead1
        # 创建一个用于返回头指针的pHead，最后返回该指针，即合并后链表的头指针
        if pHead1.data < pHead2.data:
            pp = pHead1
            pHead1 = pHead1.next
        else:
            pp = pHead2
            pHead2 = pHead2.next
        # 此p用于移动
        p = pp
        while pHead1 and pHead2:
            if pHead1.data < pHead2.data:
                p.next = pHead1
                pHead1 = pHead1.next
            else:
                p.next = pHead2
                pHead2 = pHead2.next
            p = p.next

        if not pHead1:
            p.next = pHead2
        if not pHead2:
            p.next = pHead1
        return pp

if __name__ == '__main__':
    # node1  = ListNode(None)
    node1  = ListNode(1)
    node2  = ListNode(3)
    node3  = ListNode(5)
    node4  = ListNode(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    # node11  = ListNode(None)
    node11  = ListNode(2)
    node22  = ListNode(4)
    node33  = ListNode(6)
    node44  = ListNode(8)
    node11.next = node22
    node22.next = node33
    node33.next = node44
    s = Solution()
    p = s.Merge(node1,node11)
    while p:
        print(p.data,end=' ')
        p = p.next