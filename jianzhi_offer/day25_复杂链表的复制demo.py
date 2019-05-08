# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""
# 解题思路：
"""要求：链表中除了指向后一个结点的指针之外，还有一个指针指向任意结点
分为三步完成：
一:复制每个结点，并把新结点放在老结点后面，如1->2,复制为1->1'->2->2'
二:为每个新结点设置random指针
三:把复制后的结点链表拆开
"""
class RandomListNode:
    def __init__(self, x,pNext=None,pSibling=None):
        self.label = x
        self.next = pNext
        self.random = pSibling

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not isinstance(pHead,RandomListNode):
            return None
        if not pHead:
            return None
        h= self.CloneStep1(pHead)
        head = self.CloneStep2(h)
        ret = self.CloneStep3(head)
        print(ret.label)
        return ret

    def CloneStep1(self,phead):
        #复制每个结点，并把新结点放在老结点后面，如1->2,复制为1->1'->2->2'
        pnode = phead
        while pnode:
            p = RandomListNode(pnode.label)
            p.label = pnode.label   #保证链表不断的插入顺序
            p.next = pnode.next     #1
            p.random = None
            pnode.next  = p         #2
            pnode = p.next          #3
        return phead

    def CloneStep2(self,phead):
        #为每个新结点设置random指针
        pnode = phead
        while pnode:
            p = pnode.next
            if pnode.random:
                p.random = pnode.random.next
            pnode = p.next
        return phead

    def CloneStep3(self,phead):
        #把复制后的结点链表拆开
        pnode = phead
        if pnode:
            clonehead = pnode.next
            p = pnode.next
            pnode.next  = p.next
            pnode = pnode.next
        while pnode:
            p.next = pnode.next
            p = p.next
            pnode.next = p.next
            pnode = pnode.next
        return clonehead

    def Print(self,pHead):
        if not isinstance(pHead, RandomListNode):
            return
        p = pHead
        while p:
            print(p.label, end=' ')
            if p.random:
                print(p.random.label,end=' ')
            else:
                print("#",end=' ')
            p = p.next
        print()

if __name__ == '__main__':
    node5 = RandomListNode(5)
    node4 = RandomListNode(4, node5)
    node3 = RandomListNode(3, node4)
    node2 = RandomListNode(2, node3)
    node1 = RandomListNode(1, node2)

    node1.random = node3
    node2.random = node5
    node4.random = node2

    s = Solution()
    p1 = s.Clone(node1)
    print("原链表：")
    s.Print(node1)
    print(type(p1))
    print("复制链表：")
    s.Print(p1)