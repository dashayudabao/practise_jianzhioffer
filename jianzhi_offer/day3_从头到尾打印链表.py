# Author: Baozi
#-*- codeing:utf-8 -*-
"""
题目：
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList
"""
#定义一个单节点
class Node:
    def __init__(self,data,p=None):
        self.data = data
        self.next = p
#定义一个空的带头结点的链表
class LinkNode:
    def __init__(self):
        self.head = Node(None)

    def create(self,data):
        if not isinstance(data,list) or len(data) == 0:
            print("List is Null!")
            return

        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            p.next = Node(i)
            p = p.next

def printListFromTailToHead(head):
    if head == None:
       print("List is Null!")
    p = head
    # print("#"*30,p)
    if p.next:
        printListFromTailToHead(p.next)
    print(head.data)

if __name__ == '__main__':
    l = [2,3,4,5,6,7,8,9]
    a = LinkNode()
    a.create(l)
    printListFromTailToHead(a.head)






