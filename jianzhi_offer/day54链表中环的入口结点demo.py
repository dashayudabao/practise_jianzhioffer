# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""
"""解题思路：
 思路是这样的：设定两个指针，一个慢指针，一个快指针，快指针的速度是慢指针的两倍，
 然后呢，如果有环，他们一定会在环中相遇。 
1）如果这时快指针已经是在环里走了一圈了（这种情况对应于非环指针较短的情况）
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        slow = pHead
        fast = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        fast = pHead
        while fast!=slow:
            slow = slow.next
            fast = fast.next
        return slow
