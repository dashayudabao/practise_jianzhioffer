# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""
"""
思路：由于栈是先进后出的数据结构，队列是先进先出的数据结构，
对于队列的Pop（删除)操作：
假设我们有两个栈分别是stack1和stack2，我们有三个元素a,b,c依次进入栈stack1中，
接下来要进行删除元素的话，根据队列的数据结构应该是删除最先进入的a元素，
但是不能直接对stack1进行pop操作，于是我们需要借助栈stack2，先将元素压入stack2中再进行pop操作即可实现，
但是需要注意的是，如果stack2中本身有元素的话直接进行pop操作即可。
对于队列Push操作：
我们直接将元素压入stack1即可，无论stack2中是否还有元素存在均不影响。
"""
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,data=None):
        if not data:
            return  #注意此处不应该写print语句应直接返回，否则的话会为stack添加一个None元素！
        self.stack1.append(data)

    def pop(self):
        if not self.stack1 and not self.stack2:
            # print("No element!")
            return
        if not self.stack2:
            length = len(self.stack1)
            for i in range(length):
                tmp = self.stack1.pop()
                self.stack2.append(tmp)

        return self.stack2.pop()

if __name__ == '__main__':
    queue =MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push()
    print("第1个元素",queue.pop())
    print("第2个元素",queue.pop())
    print("第3个元素",queue.pop())
    # print(queue.pop())
    queue.push(10)
    queue.push(11)
    queue.push(12)
    # print(queue.stack1)
    # print(queue.stack2)
    print("第4个元素",queue.pop())
    print("第5个元素",queue.pop())
    print("第6个元素",queue.pop())