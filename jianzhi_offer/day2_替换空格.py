# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
"""
str = " W earehapp y ! "
print(str.replace(' ','%20'))
"""
str1 = ""
space_s = 0
for i in str:
    if i == " ":
        space_s += 1
final_length = str.__len__() + space_s * 2
print("原始字符串str为：",str)
print("原始字符串长度：",str.__len__())
print("空格个数",space_s)
print("预估最终长度",final_length)
p1 = str.__len__() - 1
p2 = final_length - 1

while(p1>= 0 and p2 >= p1):
    if str[p1] != " ":
        str1 = str[p1] + str1
        p2 -= 1
    else:
        #将一个字符串中的每个空格替换成“%20”
        str1 = "0" + str1
        p2 -= 1
        str1 = "2" + str1
        p2 -= 1
        str1 = "%" + str1
        p2 -= 1
    p1 -= 1
# print(str[p1],p2)
print("实际最终字符串str1为：",str1)
print("实际最终字符串str1长度为：",str1.__len__())

"""