# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述：
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""
"""解题方法
要删除有序链表中所有的重复节点，而头结点有可能就是重复节点。这样的比较好的解决方式就是新建头结点，
然后往后遍历，同样的值就全部略过
"""
class ListNode:
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        first = ListNode(None)
        first.next = pHead
        last,cur = first,pHead
        while cur and cur.next:
            if cur.val != cur.next.val:
                last = last.next
                cur = cur.next
            else:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                last.next = cur
        return first.next



