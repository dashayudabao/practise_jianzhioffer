# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入一个链表，反转链表后，输出新链表的表头。
"""
#思路1：为了反转链表，同时我们要保证我们需要在转换的过程中我们需要三个指针：
# 即不仅要记住当前节点，也需要记住前一个节点和后一个节点。
#思路2：头插法
#思路3：利用栈，第一次将
class ListNode:
    def __init__(self, data,next=None):
        self.data = data
        self.next = next

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not isinstance(pHead,ListNode):
            return None
        if not pHead or not pHead.next:
            return pHead
        head = pHead
        then = head.next
        head.next = None
        last = then.next
        while then:
            then.next = head
            head = then
            then = last
            if then:
                last = then.next
        return head
if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    s = Solution()
    p = s.ReverseList(node1)
    while p:
        print(p.data,end=' ')
        p = p.next


