# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入一个链表，输出该链表中倒数第k个结点
"""
#思路1：遍历链表求得其长度length后，第二次遍历输出length-k指代的节点即可。
#思路2：利用快慢指针，快指针为p1,慢指针为p2，快指针p1先指向头结点然后向后遍历，
# 遍历k-1个位置后，然后同时慢p2指针也开始向后遍历，直至快指针遍历结束的时候，
# 慢指针即指向我们的倒数第k个位置。
class ListNode:
    def __init__(self, data,next= None):
        self.val = data
        self.next = next

class Solution:
    def FindKthToTail(self, head, k):
        if not isinstance(head,ListNode) or not head :
            print("链表输入有误！")
            return
        if not isinstance(k,int) or k<=0:
            print("k值输入有误！")
            return

        p1 = head
        p2 = head
        while p1 and k-1 > 0:
            p1 = p1.next
            k -= 1
        if not p1 :#此时代表k值比链表总长还长
            print("k值输入过大！")
            return

        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        return p2.val


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    # node6 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # node5.next = node6

    # List_Print(node1)
    s = Solution()
    print(isinstance(node1,ListNode))
    print(s.FindKthToTail(node1,0))
    print(s.FindKthToTail(node1,1))
    print(s.FindKthToTail(node1,2))
    print(s.FindKthToTail(node1,3))
    print(s.FindKthToTail(node1,4))
    print(s.FindKthToTail(node1,5))
    print(s.FindKthToTail(node1,6))
    print(s.FindKthToTail(node1,7))
    print(s.FindKthToTail(node1,8))

    # FindListMiddle(node1)


